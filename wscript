# vim: set fileencoding=UTF-8 filetype=python :

VERSION='0.1.0'
APPNAME='latex-examples'

top = '.'
out = 'build'

def options(opt):
    opt.load('tex')
    opt.add_option('--lore', action='store_true', default=False, 
                   help='add commandline arguments for silent vim compilation')

def configure(conf):
    conf.load('tex')
    if not conf.env.PDFLATEX:
        conf.fatal('Could not find the program pdflatex.')
    if conf.options.lore:
        conf.env.PDFLATEXFLAGS += ['-file-line-error', '-interaction=nonstopmode']

def build(bld):
    # compile tikz figures
    bld.recurse('tikz')
    bld.recurse('tikz-qkd-attack')
    
