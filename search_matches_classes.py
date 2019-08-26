import click
import os
import re
import shlex
import subprocess
from pathlib import Path

class Config(object):
    pass

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--regex', '-r',
              help="inset search keyword/regex pattern,\n"
                   "A multiple strig should be in quotation marks,\n"
                   "example: 'find me'")
@click.option('--color', '-c', default='red',
              help="choose matched text color")

@click.option('--underline', '-u', is_flag=True,
              help="add underline to the matched text")
@pass_config
def cli(config, regex, color, underline):
    '''
    \b
    info: sreach_matches application simply search
    and display pattern matches in file/s or stdout'''

    config.regex = regex
    config.color = color
    config.underline = underline

@cli.command()
@click.argument('input')
@pass_config
def stdin(config, input):
    """
    this command accept stdin same as in shell command line

    examples:

    \b
    history:
    stdin history

    \b
    ls -a:
    stdin 'ls -a'

    \b
    NOTE:
        A command with multiple parameters should be in quotation marks, e.g. 'ls -a'

    """
    if input == 'history':
        home = str(Path.home())
        with open(home + '/.bash_history', 'r') as file:
            output = file.read()
        input = None
        m = SearchMatches(input, output, config.regex, config.color, config.underline)
        m.print_match_lines()
    else:
        input = shlex.split(input)
        output = subprocess.check_output(input).decode('ascii')
        input = None
        m = SearchMatches(input, output, config.regex, config.color, config.underline)
        m.print_match_lines()

@cli.command()
@click.argument('input', type=click.File('r'), nargs=-1)
@pass_config
def cat(config, input):
    """
    this command works similar to the Unix `cat` command

    examples:

    \b
    cat single file:
    cat file.txt

    \b
    cat multiple files:
    cat file.txt file1.txt file2.txt
    """
    for file in input:
        while True:
            output = file.read()
            if not output:
                break
            m = SearchMatches(file, output, config.regex, config.color, config.underline)
            m.print_match_lines()


class SearchMatches:
    def __init__(self, input, output, regex, color, underline):
        self.input = input
        self.output = output
        self.regex = regex
        self.color = color
        self.underline = underline

    def print_match_lines(self):
        self.output = iter(self.output.splitlines())
        line_num = 0
        num_of_matches = 0
        for readline in self.output:
            line_num += 1
            if self.regex in self.mark_matches(readline):
                num_of_matches += 1
                self.print_convention(line_num, readline)
        if num_of_matches == 0:
            print('No matches found')

    def mark_matches(self, readline):
        return re.sub(self.regex, self.text_style(), readline)

    def text_style(self):
        return click.style(f'{self.regex}', fg=self.color, underline=self.underline)

    def start_pos(self, readline):
        pos = re.search(self.regex, readline)
        return pos.start()

    def mark_multi_matches(self, readline):  # handle regex pattern
        finds = list(dict.fromkeys(re.findall(self.regex, readline)))
        for regex in finds:
            self.regex = regex
            readline = self.mark_matches(readline)
        return readline

    def print_convention(self, line_num, readline):
        if input is None:
            print(f'line:{line_num} start_positon:{self.start_pos(readline)} '
                  f'matched_text:{self.mark_multi_matches(readline)}')  # stdin convention
        else:
            filename, file_extension = os.path.splitext(self.input.name)
            print(f'format:{file_extension} file_name:{filename} line:{line_num} start_positon:{self.start_pos(readline)} '
                  f'matched_text:{self.mark_multi_matches(readline)}')  # file convention
