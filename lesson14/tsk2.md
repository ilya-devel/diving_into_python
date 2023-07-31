
    >>> from tsk1 import clear_text

    >>> clear_text("some text") == "some text"
    True

    >>> clear_text("Some text") == "some text"
    True

    >>> clear_text("some, text") == "some text"
    True

    >>> clear_text("Наверное:some text") == "some text"
    True

    >>> clear_text("SoМme text!") == "some text"
    True