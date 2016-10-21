from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def documentation(request):
    generator = schemas.SchemaGenerator(title='Export Directory API')
    return response.Response(generator.get_schema(request=request))