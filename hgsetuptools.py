"""
A hook into setuptools for the mercurial version control system.

See:
http://peak.telecommunity.com/DevCenter/setuptools#adding-support-for-other-revision-control-systems

"""

__author__ = 'Maris Fogels <mfogels at gmail com>'

__DEBUG__ = False

def find_hg_files(dirname):
    '''
    Yield all files that mercurial has under source control under
    dirname.
    '''
    try:
        from mercurial import hg, ui
    except:
        # I know this is evil, but mercurial has a tendancy to fail in
        # very mysterious ways, particularly with errors about
        # meta-class internals.
        if __DEBUG__: raise
        return

    ui = ui.ui()
    try:
        repo = hg.repository(ui, dirname)
    except hg.RepoError:
        # oops, maybe we are running in a directory that is not under
        # the control of a mercurial repository?
        if __DEBUG__: raise
        return

    # tuple of (modified, added, removed, deleted, unknown, ignored, clean)
    removed = repo.status()[2]
    deleted = repo.status()[3]
    unknown = repo.status()[4]

    # exclude all files that hg knows about, but haven't been added,
    # or have been deleted, removed, or deleted
    excluded = removed + deleted + unknown
    vcfiles = lambda f: f not in excluded
    
    for _, fn in repo.walk(match=vcfiles):
        yield fn
