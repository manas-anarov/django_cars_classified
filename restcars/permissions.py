from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
	message = "You must be owner of this object."
	def has_object_permission(self, request, veiw, obj):
		return obj.profile == request.user