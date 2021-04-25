from rest_framework.mixins import CreateModelMixin


class CreateManyModelMixin(CreateModelMixin):
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateManyModelMixin, self).get_serializer(*args, **kwargs)  # Noqa

