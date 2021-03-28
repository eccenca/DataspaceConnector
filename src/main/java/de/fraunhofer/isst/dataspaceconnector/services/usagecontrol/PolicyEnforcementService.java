package de.fraunhofer.isst.dataspaceconnector.services.usagecontrol;

import de.fraunhofer.iais.eis.ContractAgreement;
import de.fraunhofer.isst.dataspaceconnector.config.ConnectorConfiguration;
import de.fraunhofer.isst.dataspaceconnector.config.UsageControlFramework;
import de.fraunhofer.isst.dataspaceconnector.exceptions.PolicyRestrictionException;
import de.fraunhofer.isst.dataspaceconnector.exceptions.ResourceNotFoundException;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.net.URI;
import java.text.ParseException;
import java.util.Arrays;

/**
 * This class implements automated policy check and usage control enforcement. Refers to the ids
 * policy enforcement point (PEP).
 */
@Service
@EnableScheduling
@RequiredArgsConstructor
public class PolicyEnforcementService {

    /**
     * Class level logger.
     */
    private static final Logger LOGGER = LoggerFactory.getLogger(PolicyEnforcementService.class);

    /**
     * Service for configuring policy settings.
     */
    private final @NonNull ConnectorConfiguration connectorConfig;

    /**
     * The policy execution point.
     */
    private final @NonNull PolicyDecisionService decisionService;

    /**
     * The delay of the scheduler.
     */
    private static final int FIXED_DELAY = 60_000;


    /**
     * Periodically (every minute) calls {@link PolicyDecisionService#scanAgreements()}.
     */
    @Scheduled(fixedDelay = FIXED_DELAY)
    public void schedule() {
        try {
            if (connectorConfig.getUcFramework() == UsageControlFramework.INTERNAL) {
                LOGGER.info("Scan resources...");
                decisionService.scanAgreements();
            }
        } catch (IllegalArgumentException | ParseException | ResourceNotFoundException exception) {
            LOGGER.warn("Failed to check policy. [exception=({})]", exception.getMessage());
        }
    }

    /**
     * Policy check on data provision on provider side.
     *
     * @param requestedElement The requested element.
     * @param agreement The ids contract agreement.
     * @throws PolicyRestrictionException If a policy restriction has been detected.
     */
    public void checkPolicyOnDataProvision(final URI requestedElement,
                                           final ContractAgreement agreement) throws PolicyRestrictionException {
        final var ignorePatterns = connectorConfig.isAllowUnsupported();
        // Ignore patterns if unknown patterns are allowed.
        if (!ignorePatterns) {
            switch (connectorConfig.getUcFramework()) {
                case MY_DATA: // Empty on purpose. TODO Needs to be implemented.
                case INTERNAL:
                default:
                    final var allowedPatterns = Arrays.asList(
                            PolicyPattern.PROVIDE_ACCESS,
                            PolicyPattern.PROHIBIT_ACCESS,
                            PolicyPattern.USAGE_DURING_INTERVAL,
                            PolicyPattern.USAGE_UNTIL_DELETION,
                            PolicyPattern.CONNECTOR_RESTRICTED_USAGE);
                    decisionService.checkForDataAccess(allowedPatterns, requestedElement, agreement);
                    break;
            }
        }
    }

    /**
     * Policy check on data access on consumer side.
     *
     * @param requestedElement The requested element.
     * @throws PolicyRestrictionException If a policy restriction has been detected.
     */
    public void checkPolicyOnDataAccess(final URI requestedElement) throws PolicyRestrictionException {
        final var ignorePatterns = connectorConfig.isAllowUnsupported();
        // Ignore patterns if unknown patterns are allowed.
        if (!ignorePatterns) {
            switch (connectorConfig.getUcFramework()) {
                case MY_DATA: // Empty on purpose. TODO Needs to be implemented.
                case INTERNAL:
                default:
                    final var allowedPatterns = Arrays.asList(
                            PolicyPattern.PROVIDE_ACCESS,
                            PolicyPattern.USAGE_DURING_INTERVAL,
                            PolicyPattern.USAGE_UNTIL_DELETION,
                            PolicyPattern.DURATION_USAGE,
                            PolicyPattern.USAGE_LOGGING,
                            PolicyPattern.N_TIMES_USAGE,
                            PolicyPattern.USAGE_NOTIFICATION);
                    decisionService.checkForDataAccess(allowedPatterns, requestedElement);
                    break;
            }
        }
    }
}
