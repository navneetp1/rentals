# always cached
no_cache = 1 # no caching

# get_context() is needed in this file
def get_context(context):
    context.message = "Hey, this is a message passed through context"