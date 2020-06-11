from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

from rest_framework.response import Response

class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    
    max_limit = 10


class PostPageNumberPagination(PageNumberPagination):
	page_size = 10
	def get_paginated_response(self, data):
		response = super(PostPageNumberPagination, self).get_paginated_response(data)
		response.data['total_pages'] = self.page.paginator.num_pages
		response.data['limit'] = self.page_size
		return response


	# def get_paginated_response(self, data):
	# 	return Response({
	# 		'next': self.get_next_link(),
	# 		'previous': self.get_previous_link(),
	# 		'count': self.page.paginator.count,
	# 		'total_pages': self.page.paginator.num_pages,
	# 		'results': data
 #        })

# class PageNumberPaginationWithCount(pagination.PageNumberPagination):
#     def get_paginated_response(self, data):
#         response = super(PageNumberPaginationWithCount, self).get_paginated_response(data)
#         response.data['total_pages'] = self.page.paginator.num_pages
#         return response