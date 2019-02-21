import builtins
from django_jinja import library # @UnresolvedImport

### functions that emulate builtins -- leave last so we are not bitten
# pylint: disable=redefined-builtin

@library.global_function
def dir(obj): # @ReservedAssignment
    '''
    Super useful for debugging...
    '''
    return str(builtins.dir(obj))

@library.global_function
def getattr(*args): # @ReservedAssignment
    return builtins.getattr(*args)

@library.global_function
def len(obj): # @ReservedAssignment
    return builtins.len(obj)
