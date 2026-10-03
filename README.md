# EnFiRCE

**EnFiRCE** (*Environment- and Friction-informed Rod Contact Estimation*) is the project page for a Georgia Tech simulation study on recovering contact and tip forces on a slender continuum rod from sparse shape measurements and planar environment constraints.

- Live page: https://enfirce.github.io/
- MATLAB code: https://github.com/universeleaf/force-sensor

This repository is a static GitHub Pages site, adapted from the [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template) / [Nerfies](https://nerfies.github.io/).

All numbers and videos on the page are offline simulations. The manuscript is a research draft with author metadata unset. Comparisons identify their adaptations and input conditions; they do not establish a universal performance ranking.

The static site uses `index.html`, `static/css/research.css`, and `static/js/research.js`. Quantitative text comes from `static/results/website_summary.json`, copied from a completed protocol. The release manifest records original paths, bytes, and SHA-256 for figures, source data, the draft PDF, and MP4s. Archived videos and the new full-window benchmark have separate solver provenance and scope.

In the MATLAB repository, the release workflow is:

```text
MATLAB: force('publication')
python scripts/render_formulation_publication.py
python scripts/update_publication_manuscript.py
python scripts/compile_publication_manuscript.py
python scripts/sync_publication_website.py
```

The synchronization script requires all inference stages, engineering checks, and figure checksums to pass. It copies real archived video bytes and does not publish with Git. Serve this directory with `python -m http.server` for local viewing; the result summary requires HTTP rather than direct `file://` access.

The manuscript build record binds the PDF to the actual TeX, bibliography, template, and figure bytes. Synchronization rejects a stale PDF after any manuscript input changes.
