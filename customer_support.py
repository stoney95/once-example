from dataclasses import dataclass, field
import string
import random
from typing import List, Callable

import logging

logger = logging.getLogger(__name__)


def generate_id(length: int = 8) -> str:
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


@dataclass
class SupportTicket:
    id: str = field(init=False, default_factory=generate_id)
    customer: str
    issue: str
    can_be_solved: bool


SupportTickets = List[SupportTicket]

Ordering = Callable[[SupportTickets], SupportTickets]


def fifo_ordering(list: SupportTickets) -> SupportTickets:
    return list.copy()


def filo_ordering(list: SupportTickets) -> SupportTickets:
    list_copy = list.copy()
    list_copy.reverse()
    return list_copy


def random_ordering(list: SupportTickets) -> SupportTickets:
    list_copy = list.copy()
    random.shuffle(list_copy)
    return list_copy


def blackhole_ordering(_: SupportTickets) -> SupportTickets:
    return []


class CustomerSupport:

    def __init__(self):
        self.tickets: SupportTickets = []

    def create_ticket(self, customer, issue, can_be_solved):
        self.tickets.append(SupportTicket(customer, issue, can_be_solved))

    def process_tickets(self, ordering: Ordering):
        # create the ordered list
        ticket_list = ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            logger.info("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        logger.info(f"Processing ticket id: {ticket.id}. Customer {ticket.customer}.")
        if not ticket.can_be_solved:
            raise RuntimeError(f"Ticket with id {ticket.id} cannot be solved.")