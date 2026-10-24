import sys
from pathlib import Path


PLAYWRIGHT_PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PLAYWRIGHT_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PLAYWRIGHT_PROJECT_ROOT))

from microsoftteams.bdd.support import close_browser


def after_scenario(context, scenario):
    close_browser(
        getattr(context, "playwright", None),
        getattr(context, "browser", None),
    )
