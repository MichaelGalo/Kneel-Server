import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

# non-boilerplate imports
from views import list_all_orders


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
        else:
            pass


#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ""
    port = 8088
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
