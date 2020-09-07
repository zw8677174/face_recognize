
class Response:

    def success(self, *args):
        if args:
            return {
                "msg": "success",
                "data": args[0]
                }

            return {
                "msg": "success",
                "data": ""
                }
