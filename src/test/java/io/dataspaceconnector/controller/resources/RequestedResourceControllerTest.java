package io.dataspaceconnector.controller.resources;

import java.net.URI;
import java.util.UUID;

import io.dataspaceconnector.model.RequestedResource;
import io.dataspaceconnector.model.RequestedResourceDesc;
import io.dataspaceconnector.services.resources.ResourceService;
import io.dataspaceconnector.services.resources.SubscriberNotificationService;
import io.dataspaceconnector.view.RequestedResourceViewAssembler;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.data.web.PagedResourcesAssembler;
import org.springframework.http.HttpStatus;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.doThrow;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;

@SpringBootTest(classes = {ResourceControllers.RequestedResourceController.class})
class RequestedResourceControllerTest {
    @MockBean
    private ResourceService<RequestedResource, RequestedResourceDesc> service;

    @MockBean
    private RequestedResourceViewAssembler assembler;

    @MockBean
    private PagedResourcesAssembler<RequestedResource> pagedAssembler;

    @MockBean
    private SubscriberNotificationService subscriberNotificationService;

    @Autowired
    @InjectMocks
    private ResourceControllers.RequestedResourceController controller;

    private final UUID resourceId = UUID.randomUUID();

    private final URI subscriberUrl = URI.create("https://subscriber.com");

    @Test
    public void create_null_returnMethodNotAllowed() {
        /* ARRANGE */
        // Nothing to arrange.

        /* ACT */
        final var result = controller.create(null);

        /* ASSERT */
        assertEquals(HttpStatus.METHOD_NOT_ALLOWED.value(), result.getStatusCodeValue());
        assertNull(result.getBody());
        Mockito.verifyNoInteractions(service);
    }

    @Test
    public void create_validDesc_returnMethodNotAllowed() {
        /* ARRANGE */
        // Nothing to arrange.

        /* ACT */
        final var result = controller.create(new RequestedResourceDesc());

        /* ASSERT */
        assertEquals(HttpStatus.METHOD_NOT_ALLOWED.value(), result.getStatusCodeValue());
        assertNull(result.getBody());
        Mockito.verifyNoInteractions(service);
    }

    @Test
    public void subscribe_resourceIdNull_throwIllegalArgumentException() {
        /* ARRANGE */
        doThrow(IllegalArgumentException.class).when(subscriberNotificationService)
                .addSubscription(eq(null), eq(subscriberUrl));

        /* ACT && ASSERT */
        assertThrows(IllegalArgumentException.class,
                () -> controller.subscribe(null, subscriberUrl));
    }

    @Test
    public void subscribe_urlNull_throwIllegalArgumentException() {
        /* ARRANGE */
        doThrow(IllegalArgumentException.class)
                .when(subscriberNotificationService).addSubscription(eq(resourceId), eq(null));

        /* ACT && ASSERT */
        assertThrows(IllegalArgumentException.class,
                () -> controller.subscribe(resourceId, null));
    }

    @Test
    public void subscribe_validInput_addSubscription() {
        /* ARRANGE */
        doNothing().when(subscriberNotificationService)
                .addSubscription(eq(resourceId), eq(subscriberUrl));

        /* ACT */
        final var result = controller.subscribe(resourceId, subscriberUrl);

        /* ASSERT */
        assertEquals(HttpStatus.OK, result.getStatusCode());
        verify(subscriberNotificationService, times(1))
                .addSubscription(resourceId, subscriberUrl);
    }

    @Test
    public void unsubscribe_resourceIdNull_throwIllegalArgumentException() {
        /* ARRANGE */
        doThrow(IllegalArgumentException.class).when(subscriberNotificationService)
                .removeSubscription(eq(null), eq(subscriberUrl));

        /* ACT && ASSERT */
        assertThrows(IllegalArgumentException.class,
                () -> controller.unsubscribe(null, subscriberUrl));
    }

    @Test
    public void unsubscribe_urlNull_throwIllegalArgumentException() {
        /* ARRANGE */
        doThrow(IllegalArgumentException.class).when(subscriberNotificationService)
                .removeSubscription(eq(resourceId), eq(null));

        /* ACT && ASSERT */
        assertThrows(IllegalArgumentException.class,
                () -> controller.unsubscribe(resourceId, null));
    }

    @Test
    public void unsubscribe_validInput_removeSubscription() {
        /* ARRANGE */
        doNothing().when(subscriberNotificationService)
                .removeSubscription(eq(resourceId), eq(subscriberUrl));

        /* ACT */
        final var result = controller.unsubscribe(resourceId, subscriberUrl);

        /* ASSERT */
        assertEquals(HttpStatus.OK, result.getStatusCode());
        verify(subscriberNotificationService, times(1))
                .removeSubscription(resourceId, subscriberUrl);
    }
}
