from .start import router as start_router
from .profile import router as profile_router
from .balance import router as balance_router
from .referral import router as referral_router
from .support import router as support_router

__all__ = (
    "start_router",
    "profile_router",
    "balance_router",
    "referral_router",
    "support_router",
)
