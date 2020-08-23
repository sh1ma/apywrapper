from cleo import Command, argument, option, Application


class HelloCommand(Command):

    name = "hello"
    description = "Say hello to someone"

    arguments = [argument("name", "Name of a person to hello")]

    def handle(self):
        self.line(f'Hello {self.argument("name")}!')


class GoodnightCommand(Command):

    name = "goodnight"
    description = "Say goodnight to someone"

    arguments = [argument("name", "Name of a person to goodnight")]
    options = [option("sleeping", "s", "Sleeping...")]

    def handle(self):
        if self.option("s"):
            self.line("zzz")
        else:
            self.line(f'Goodnight {self.argument("name")}...')


application = Application()
application.add_commands(HelloCommand(), GoodnightCommand())


def main():
    application.run()
