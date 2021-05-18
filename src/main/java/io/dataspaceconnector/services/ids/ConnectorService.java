/*
 * Copyright 2020 Fraunhofer Institute for Software and Systems Engineering
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package io.dataspaceconnector.services.ids;

import java.net.URI;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import java.util.stream.Collectors;

import de.fraunhofer.iais.eis.BaseConnector;
import de.fraunhofer.iais.eis.BaseConnectorImpl;
import de.fraunhofer.iais.eis.ConfigurationModelImpl;
import de.fraunhofer.iais.eis.DynamicAttributeToken;
import de.fraunhofer.iais.eis.Resource;
import de.fraunhofer.iais.eis.ResourceCatalog;
import de.fraunhofer.iais.eis.util.ConstraintViolationException;
import de.fraunhofer.isst.ids.framework.configuration.ConfigurationContainer;
import de.fraunhofer.isst.ids.framework.configuration.ConfigurationUpdateException;
import de.fraunhofer.isst.ids.framework.daps.DapsTokenProvider;
import io.dataspaceconnector.model.OfferedResource;
import io.dataspaceconnector.services.ids.builder.IdsCatalogBuilder;
import io.dataspaceconnector.services.ids.builder.IdsResourceBuilder;
import io.dataspaceconnector.services.resources.CatalogService;
import io.dataspaceconnector.services.resources.OfferedResourceService;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

/**
 * This service offers different methods related to the connector configuration, like e.g. getting
 * configuration properties or updating the configuration model.
 */
@Log4j2
@Service
@RequiredArgsConstructor
public class ConnectorService {

    /**
     * The current connector configuration.
     */
    private final @NonNull ConfigurationContainer configContainer;

    /**
     * The token provider.
     */
    private final @NonNull DapsTokenProvider tokenProvider;

    /**
     * Service for persisted catalogs.
     */
    private final @NonNull CatalogService catalogService;

    /**
     * Service for ids views.
     */
    private final @NonNull IdsCatalogBuilder catalogBuilder;

    /**
     * Service for ids resources.
     */
    private final @NonNull IdsResourceBuilder<OfferedResource> resourceBuilder;

    /**
     * Service for offered resources.
     */
    private final @NonNull OfferedResourceService offeredResourceService;

    /**
     * Get a local copy of the current connector and extract its id.
     *
     * @return The connector id.
     */
    public URI getConnectorId() {
        final var connector = configContainer.getConnector();
        return connector.getId();
    }

    /**
     * Get a local copy of the current connector and extract the outbound model version.
     *
     * @return The outbound model version.
     */
    public String getOutboundModelVersion() {
        final var connector = configContainer.getConnector();
        return connector.getOutboundModelVersion();
    }

    /**
     * Get a local copy of the current connector and extract the inbound model versions.
     *
     * @return A list of supported model versions.
     */
    public List<? extends String> getInboundModelVersion() {
        final var connector = configContainer.getConnector();
        return connector.getInboundModelVersion();
    }

    /**
     * Return current DAT.
     *
     * @return The connector's DAT.
     */
    public DynamicAttributeToken getCurrentDat() {
        return tokenProvider.getDAT();
    }

    /**
     * Build a base connector object with all offered resources.
     *
     * @return The ids base connector object.
     */
    public BaseConnector getConnectorWithOfferedResources() throws ConstraintViolationException {
        // Get a local copy of the current connector.
        final var connector = configContainer.getConnector();
        final var catalogs = getAllCatalogsWithOfferedResources();

        // Create a connector with a list of offered resources.
        final var connectorImpl = (BaseConnectorImpl) connector;
        connectorImpl.setResourceCatalog(catalogs);
        return connectorImpl;
    }

    /**
     * Build a base connector object without resources.
     *
     * @return The ids base connector object.
     */
    public BaseConnector getConnectorWithoutResources() throws ConstraintViolationException {
        // Get a local copy of the current connector.
        final var connector = configContainer.getConnector();

        // Create a connector without any resources.
        final var connectorImpl = (BaseConnectorImpl) connector;
        connectorImpl.setResourceCatalog(null);
        return connectorImpl;
    }

    /**
     * Updates the connector object in the ids framework's config container.
     *
     * @throws ConfigurationUpdateException If the configuration could not be update.
     */
    public void updateConfigModel() throws ConfigurationUpdateException {
        try {
            final var connector = getConnectorWithOfferedResources();
            final var configModel = (ConfigurationModelImpl) configContainer.getConfigModel();
            configModel.setConnectorDescription(connector);

            // Handled at a higher level.
            configContainer.updateConfiguration(configModel);
        } catch (ConstraintViolationException e) {
            if (log.isWarnEnabled()) {
                log.warn("Failed to retrieve connector. [exception=({})]", e.getMessage(), e);
            }
            throw new ConfigurationUpdateException("Failed to retrieve connector.", e);
        }
    }

    /**
     * Get all catalogs with offered resources.
     *
     * @return List of resource catalogs.
     */
    private List<ResourceCatalog> getAllCatalogsWithOfferedResources() {
        return catalogService.getAll(Pageable.unpaged())
                .stream()
                .map(x -> catalogBuilder.create(x, 0))
                .filter(Objects::nonNull)
                .collect(Collectors.toList());
    }

    /**
     * Get offered resource by its id.
     *
     * @param resourceId The resource id.
     * @return The ids resource.
     */
    public Optional<Resource> getOfferedResourceById(final URI resourceId) {
        final var resource = offeredResourceService.getAll(Pageable.unpaged())
                .stream()
                .filter(x -> resourceId.toString().contains(x.getId().toString()))
                .findAny();

        return resource.map(resourceBuilder::create);
    }
}
