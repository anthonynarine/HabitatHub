from .models import Ticket
from .serializers import TicketSerializer
from rest_framework import viewsets, filters


class TicketViewset(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """
        If the user is a ticket handler, they see all tickets.
        Otherwise, users see only the tickets they've created.
        """
        user = self.request.user
        if user.groups.filter(name='Ticket Handlers').exists():
            return Ticket.objects.all()
        return Ticket.objects.filter(created_by=user)

