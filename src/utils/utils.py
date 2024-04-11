# You can create a class or directly functions
# all the common utilities we keep in this file like CSV files, env files, auth related etc
# these are not static method, we will create object of utils
class Util(object):

    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    # suppose in future we need application XML, keep below function
    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/xml",
        }
        return headers

    def common_headers_put_delete_patch_basic_auth(self, basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            #"Authorization" : "Basic YWRtaW46cGFzc3dvcmQxMjM=" # you can use like this also
            "Authorization": "Basic" + str(basic_auth_value),
            # there are 2 ways to authenticate, you can use basic auth or else cookie
        }
        return headers

    def common_headers_put_delete_patch_cookie(self, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
        }
        return headers

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database(self):
        pass

# util = Util().common_headers_json() # these are not static method, we will create object of utils, we will use in future
