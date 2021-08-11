"""TLDR SO FAR:

yield from allows us to refactor generators and chain them together.
Concept of coroutines (pausible functions)
"""

def yield_from_example():
    """Show use of yield from
    """
    print("Lazy range up to 5 with yield from iterator:")
    def lazy_range(up_to):
        """Generator to return the sequence of integers from 0 to up_to, exclusive."""
        index = 0
        def gratuitous_refactor():
            nonlocal index
            while index < up_to:
                yield index
                index += 1
        # yield from allows you to yield every value from an interator
        yield from gratuitous_refactor()

    # Pring lazy range values up to 5
    for e in lazy_range(5):
        print(e)

yield_from_example()

def chain_generator_example():
    """Shows how you can yield up and down the call stack
    """
    print("Up and down the call stack with chaining generators")
    def bottom():
        # Returning the yield lets the value that goes up the call stack to come right back
        # down.
        print("BOT CALL FRAME")
        return (yield 42)

    def middle():
        print("MID CALL FRAME")
        return (yield from bottom())

    def top():
        print("TOP CALL FRAME")
        return (yield from middle())

    # Get the generator.
    gen = top()
    value = next(gen)
    print(value)  # Prints '42'.
    try:
        value = gen.send(value * 2) # Send changes the jump value
    except StopIteration as exc:
        value = exc.value
    print(value)  # Prints '84'.

chain_generator_example()

