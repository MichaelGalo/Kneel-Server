import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

# non-boilerplate imports
from views import list_all_orders, get_order, create_order


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


#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ""
    port = 8088
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
