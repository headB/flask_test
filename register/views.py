from register import register



@register.route("/bule_print_test")
def index_test():

    return "hello,I am index_test"