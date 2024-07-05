import logging
import once

import customer_support
import coding_guidelines

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # create the application
    app = customer_support.CustomerSupport()

    # register a few tickets
    app.create_ticket("John Smith", "My computer makes strange sounds!", can_be_solved=True)
    app.create_ticket("Linus Sebastian",
                      "I can't upload any videos, please help.", can_be_solved=True)
    app.create_ticket(
        "Arjan Egges", "VSCode doesn't automatically solve my bugs.", can_be_solved=False)

    # process the tickets
    app.process_tickets(customer_support.random_ordering)


if __name__ == '__main__':
    (
        once.and_for_all.Functions()
        .apply_decorator(coding_guidelines.log_exception)
        .apply_decorator(coding_guidelines.debug_function_call)
    )
    (
        once.and_for_all.Classes()
        .and_only_their_methods()
        .apply_decorator(coding_guidelines.log_exception)
        .apply_decorator(coding_guidelines.debug_function_call)
    )
    main()