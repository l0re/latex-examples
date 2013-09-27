# vim: set fileencoding=UTF-8 filetype=python :
from os.path import basename, splitext

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def bld_and_copy(bld, name_without_ext):
    # strip extenstion
    #name, ext = splitext(mainfile)
    name = name_without_ext

    # make main document
    bld(
        features = 'tex',
        type     = 'pdflatex',
        source   = '{}.tex'.format(name),
        outs     = 'pdf',
        prompt   = 1, 
        )
    
    # copy to src dir
    bld(
        rule   = 'cp ${SRC} ${TGT}',
        source = bld.path.get_bld().make_node('{}.pdf'.format(name)),
        target = bld.path.make_node('{}.pdf'.format(name)),
    )

