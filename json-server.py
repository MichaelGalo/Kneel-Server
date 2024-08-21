import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

# non-boilerplate imports
from views import (
    list_all_orders,
    get_order,
    create_order,
    delete_order,
    update_metal,
    update_size,
    update_style,
    update_jewelry,
)


class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests for kneel diamonds"""

    def do_GET(self):
        """Handle GET requests"""

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            if url["pk"] == 0:
                response_body = list_all_orders()
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            elif url["pk"] != 0:
                response_body = get_order(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

    def do_POST(self):
        """Handle POST requests"""

        url = self.parse_url(self.path)

        # Get the request body JSON for the new data
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "orders":
            successfully_created = create_order(request_body)
            if successfully_created:
                return self.response(
                    "Your order has been created.",
                    status.HTTP_201_SUCCESS_CREATED.value,
                )
            else:
                return self.response(
                    "Your order could not be created.",
                    status.HTTP_500_SERVER_ERROR.value,
                )

    def do_DELETE(self):
        """Handle DELETE requests"""

        url = self.parse_url(self.path)
        pk = url["pk"]

        if url["requested_resource"] == "orders":
            if pk != 0:
                successfully_deleted = delete_order(pk)
                if successfully_deleted:
                    return self.response(
                        "Your order has been deleted.",
                        status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value,
                    )
                else:
                    return self.response(
                        "Your order could not be deleted.",
                        status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                    )

    def do_PUT(self):
        """Handle PUT requests"""

        url = self.parse_url(self.path)

        # Get the request body JSON for the new data
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "metals":
            successfully_updated = update_metal(url["pk"], request_body)
            if successfully_updated:
                return self.response(
                    "The metal has been updated.",
                    status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value,
                )
            else:
                return self.response(
                    "The metal could not be updated.",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )

        elif url["requested_resource"] == "sizes":
            successfully_updated = update_size(url["pk"], request_body)
            if successfully_updated:
                return self.response(
                    "The size has been updated.",
                    status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value,
                )
            else:
                return self.response(
                    "The size could not be updated.",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )

        elif url["requested_resource"] == "style":
            successfully_updated = update_style(url["pk"], request_body)
            if successfully_updated:
                return self.response(
                    "The style has been updated.",
                    status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value,
                )
            else:
                return self.response(
                    "The style could not be updated.",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )

        elif url["requested_resource"] == "jewelry":
            successfully_updated = update_jewelry(url["pk"], request_body)
            if successfully_updated:
                return self.response(
                    "The jewelry has been updated.",
                    status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value,
                )
            else:
                return self.response(
                    "The jewelry could not be updated.",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )


#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ""
    port = 8088
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
