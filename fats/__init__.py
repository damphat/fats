def interact(local=None):
    if local is None:
        import inspect
        frame = inspect.currentframe().f_back
        local = frame.f_locals
    
    import code
    import os
    import readline
    import rlcompleter
    readline.parse_and_bind("tab: complete")

    HISTORY_FILE = os.path.expanduser("./.history")
    if os.path.exists(HISTORY_FILE):
        readline.read_history_file(HISTORY_FILE)

    def save_history():
        readline.write_history_file(HISTORY_FILE)

    readline.set_pre_input_hook(save_history)

    code.interact(banner="", local=local)


