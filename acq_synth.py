# === KEEP ORIGINAL SCHEMA ON acquisitions ===
# ОРИГИНАЛЬНЫЕ ПОЛЯ acquisitions (точные названия):
# customer_id, account_id, card_id, signup_date,
# gender, age, age_band, segment, region, city,
# product, card_scheme, acquisition_channel, campaign,
# income_band, kyc_level, is_salaried, is_digital_onboarding, is_referred,
# activated_within_30d, n_txn_first_30d, spend_first_90d_sar,
# fee_revenue_90d_sar, cashback_90d_sar, active_90d, churn_90d

from __future__ import annotations
from typing import List, Dict, Tuple
import numpy as np, pandas as pd, uuid, random, hashlib

__all__ = [
    "generate_dataset",          # -> (acquisitions, dim_date, monthly_targets)
    "save_csvs",
    "plan_monthly_targets",      # monthly_targets with 'target'
    "generate_acquisitions",     # ORIGINAL SCHEMA (no target/year_month)
    "generate_dim_date",
    "generate_subproduct_dim",   # separate dataset (join by card_id)
    "save_subproducts_csv",
]

# ---------- helpers ----------
def _month_range(start_date: pd.Timestamp, end_date: pd.Timestamp) -> List[pd.Timestamp]:
    months, cur, last = [], pd.Timestamp(start_date.year, start_date.month, 1), pd.Timestamp(end_date.year, end_date.month, 1)
    while cur <= last:
        months.append(cur); cur = cur + pd.offsets.MonthBegin(1)
    return months

def _seasonal_multiplier(dt: pd.Timestamp) -> float:
    sine = np.sin((dt.month - 1) / 12 * 2 * np.pi)
    return float((1.0 + 0.08 * sine) * (1.05 if dt.month in (4,5,6,11,12) else 1.0))

def _trend_multiplier(dt: pd.Timestamp, start_dt: pd.Timestamp, end_dt: pd.Timestamp) -> float:
    total = (end_dt.year - start_dt.year) * 12 + (end_dt.month - start_dt.month)
    cur = (dt.year - start_dt.year) * 12 + (dt.month - start_dt.month)
    return 1.0 if total <= 0 else 1.0 + 0.2 * (cur / total)

def _choose(options: List, probs: List[float]): return np.random.choice(options, p=probs)
def _age_band(age: int) -> str:
    if age < 22: return "18-21"
    if age < 26: return "22-25"
    if age < 31: return "26-30"
    if age < 41: return "31-40"
    if age < 51: return "41-50"
    if age < 61: return "51-60"
    return "61-70"

def _build_region_lookup() -> Dict[str, List[str]]:
    return {
        "Riyadh": ["Riyadh"],
        "Makkah": ["Jeddah", "Makkah", "Taif"],
        "Eastern": ["Dammam", "Khobar", "Dhahran"],
        "Madinah": ["Madinah"],
        "Qassim": ["Buraydah"],
        "Asir": ["Abha", "Khamis Mushait"],
        "Tabuk": ["Tabuk"],
        "Hail": ["Hail"],
    }

# ---------- monthly targets (separate dataset; column name = 'target') ----------
def plan_monthly_targets(
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    min_month: int,
    max_month: int,
    target_multiplier: float = 1.05,
    target_jitter: float = 0.03,
) -> pd.DataFrame:
    """returns: year_month, month_start, expected_actual, target"""
    months = _month_range(start_date, end_date)
    rows = []
    for m in months:
        base = np.random.randint(min_month, max_month + 1)
        expected = int(base * _seasonal_multiplier(m) * _trend_multiplier(m, months[0], end_date))
        expected = max(expected, int(0.7 * min_month))
        factor = np.random.normal(loc=target_multiplier, scale=target_jitter)
        tgt = int(max(0, round(expected * factor)))
        rows.append({
            "year_month": m.strftime("%Y-%m"),
            "month_start": m.date(),
            "expected_actual": expected,
            "target": tgt,  # <-- ВАЖНО: имя колонки 'target'
        })
    return pd.DataFrame(rows)

# ---------- acquisitions (ORIGINAL SCHEMA; no extra columns) ----------
def generate_acquisitions(
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    min_month: int,
    max_month: int,
) -> pd.DataFrame:
    regions = list(_build_region_lookup().keys())
    region_cities = _build_region_lookup()
    genders  = ["Male", "Female"]
    segments = ["Mass", "Affluent", "Private Banking", "SME", "Student", "Expat"]
    channels = ["Branch", "Digital", "Partner", "Campaign", "Referral", "Kiosk"]
    campaigns = ["Summer CashBack 2022","Back-to-School 2023","Ramadan Rewards 2024","Travel Miles 2024","Digital Onboarding 2025","Salary Transfer 2025"]
    products = ["Debit", "Credit", "Prepaid"]
    card_schemes = ["Visa", "mada", "Dual"]
    income_bands = ["<3k","3-7k","7-15k","15-30k","30k+"]
    kyc_levels  = ["Basic","Full","Enhanced"]

    months = _month_range(start_date, end_date)
    recs, cid = [], 1

    for m in months:
        base = np.random.randint(min_month, max_month + 1)
        vol  = int(base * _seasonal_multiplier(m) * _trend_multiplier(m, months[0], end_date))
        vol  = max(vol, int(0.7 * min_month))

        for _ in range(vol):
            channel = _choose(channels, [0.28,0.34,0.12,0.14,0.07,0.05])
            gender  = _choose(genders, [0.63,0.37])

            if channel == "Digital": age = int(np.clip(np.random.normal(29,7), 18, 70))
            elif channel == "Branch": age = int(np.clip(np.random.normal(36,9), 18, 70))
            else: age = int(np.clip(np.random.normal(33,8), 18, 70))

            if age < 24: seg = _choose(segments, [0.30,0.04,0.01,0.05,0.50,0.10])
            elif age > 45: seg = _choose(segments, [0.40,0.25,0.10,0.10,0.01,0.14])
            else: seg = _choose(segments, [0.50,0.18,0.03,0.10,0.06,0.13])

            region = np.random.choice(regions)
            city   = np.random.choice(region_cities[region])

            product = _choose(products, [0.62,0.28,0.10])
            if product == "Debit": scheme = _choose(card_schemes, [0.35,0.55,0.10])
            elif product == "Credit": scheme = _choose(card_schemes, [0.80,0.05,0.15])
            else: scheme = _choose(card_schemes, [0.60,0.25,0.15])

            if seg in ("Affluent","Private Banking"):
                income = _choose(income_bands, [0.00,0.05,0.25,0.35,0.35])
            elif seg == "Student":
                income = _choose(income_bands, [0.35,0.45,0.18,0.02,0.00])
            else:
                income = _choose(income_bands, [0.08,0.25,0.40,0.20,0.07])

            if channel=="Branch" or seg in ("Affluent","Private Banking"):
                kyc = _choose(kyc_levels, [0.10,0.55,0.35])
            else:
                kyc = _choose(kyc_levels, [0.25,0.60,0.15])

            campaign = np.random.choice(campaigns) if (channel=="Campaign" or np.random.rand() < 0.25 * _seasonal_multiplier(m)) else None
            is_salaried = bool(np.random.rand() < 0.55)
            is_digital  = (channel=="Digital")
            referred    = bool(np.random.rand() < (0.25 if channel=="Referral" else 0.05))

            base_act = 0.72 + (0.05 if is_digital else 0.02) + (0.04 if kyc=="Enhanced" else (0.02 if kyc=="Full" else -0.04))
            activated_30d = bool(np.random.rand() < np.clip(base_act, 0.4, 0.95))

            mu_txn = 2.2 + (0.8 if product=="Credit" else 0.0) + (0.9 if seg in ("Affluent","Private Banking") else 0.0)
            if not activated_30d: mu_txn *= 0.4
            n_txn_30d = int(max(0, np.random.poisson(mu_txn)))

            spend_mu = 450 + (300 if product=="Credit" else 0) + (250 if seg=="Affluent" else 0) + (600 if seg=="Private Banking" else 0)
            if not activated_30d: spend_mu *= 0.35
            spend_90d = float(max(0, np.random.normal(spend_mu, spend_mu*0.5)))

            fee_rate = 0.006 if product=="Credit" else 0.004
            fee_rev  = float(spend_90d*fee_rate + (10 if product=="Credit" else 2)*(n_txn_30d>0))
            cashback = float(spend_90d * (0.005 if campaign else 0.002))

            active_90d = bool(np.random.rand() < (0.82 if activated_30d else 0.35))
            churn_90d  = not active_90d

            recs.append({
                "customer_id": f"C{cid:08d}",
                "account_id": uuid.uuid4().hex[:12].upper(),
                "card_id": uuid.uuid4().hex[:12].upper(),
                "signup_date": (m + pd.Timedelta(days=int(np.random.randint(0, 28)))).date(),

                "gender": gender,
                "age": age,
                "age_band": _age_band(age),
                "segment": seg,
                "region": region,
                "city": city,

                "product": product,
                "card_scheme": scheme,
                "acquisition_channel": channel,
                "campaign": campaign,

                "income_band": income,
                "kyc_level": kyc,
                "is_salaried": is_salaried,
                "is_digital_onboarding": is_digital,
                "is_referred": referred,

                "activated_within_30d": activated_30d,
                "n_txn_first_30d": n_txn_30d,
                "spend_first_90d_sar": round(spend_90d, 2),
                "fee_revenue_90d_sar": round(fee_rev, 2),
                "cashback_90d_sar": round(cashback, 2),
                "active_90d": active_90d,
                "churn_90d": churn_90d,
            })
            cid += 1

    acq = pd.DataFrame.from_records(recs)
    # жёстко фиксируем порядок колонок (как в первом варианте)
    cols = [
        "customer_id","account_id","card_id","signup_date",
        "gender","age","age_band","segment","region","city",
        "product","card_scheme","acquisition_channel","campaign",
        "income_band","kyc_level","is_salaried","is_digital_onboarding","is_referred",
        "activated_within_30d","n_txn_first_30d","spend_first_90d_sar",
        "fee_revenue_90d_sar","cashback_90d_sar","active_90d","churn_90d"
    ]
    return acq[cols]

# ---------- dim_date ----------
def generate_dim_date(start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
    dd = pd.DataFrame({"date": pd.date_range(start=start_date, end=end_date, freq="D")})
    dd["date_key"] = dd["date"].dt.strftime("%Y%m%d").astype(int)
    dd["year"] = dd["date"].dt.year
    dd["month"] = dd["date"].dt.month
    dd["day"] = dd["date"].dt.day
    dd["month_name"] = dd["date"].dt.month_name()
    dd["quarter"] = dd["date"].dt.quarter
    dd["year_month"] = dd["date"].dt.to_period("M").astype(str)
    dd["week"] = dd["date"].dt.isocalendar().week.astype(int)
    dd["weekday"] = dd["date"].dt.day_name()
    dd["is_month_end"] = dd["date"].dt.is_month_end
    dd["is_month_start"] = dd["date"].dt.is_month_start
    dd["YearMonthSort"] = dd["date"].dt.to_period("M").dt.start_time
    return dd

# ---------- public: dataset & saving ----------
def generate_dataset(
    start: str = "2022-01-01",
    end: str = "2025-09-30",
    min_month: int = 1200,
    max_month: int = 2800,
    seed: int | None = 42,
    target_multiplier: float = 1.05,
    target_jitter: float = 0.03,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if seed is not None:
        np.random.seed(seed); random.seed(seed)
    start_date, end_date = pd.Timestamp(start), pd.Timestamp(end)
    acq = generate_acquisitions(start_date, end_date, min_month, max_month)  # ORIGINAL SCHEMA
    dim_date = generate_dim_date(start_date, end_date)
    monthly_targets = plan_monthly_targets(start_date, end_date, min_month, max_month,
                                           target_multiplier=target_multiplier, target_jitter=target_jitter)  # has 'target'
    return acq, dim_date, monthly_targets

def save_csvs(acq: pd.DataFrame, dim_date: pd.DataFrame, monthly_targets: pd.DataFrame, outdir: str = "."):
    outdir = outdir.rstrip("/\\")
    acq.to_csv(f"{outdir}/acquisitions.csv", index=False, encoding="utf-8")
    dim_date.to_csv(f"{outdir}/dim_date.csv", index=False, encoding="utf-8")
    monthly_targets.to_csv(f"{outdir}/monthly_targets.csv", index=False, encoding="utf-8")

# ---------- subproducts (separate dataset; join by card_id) ----------
def _subproduct_probs(product: str, segment: str | None = None):
    import numpy as np
    if product == "Credit": base = np.array([0.25,0.50,0.25])
    elif product == "Debit": base = np.array([0.70,0.25,0.05])
    else: base = np.array([0.85,0.14,0.01])
    if segment in ("Affluent","Private Banking"): base = np.clip(base + np.array([-0.06,0.04,0.02]), 0, None)
    elif segment == "Student": base = np.clip(base + np.array([0.05,-0.04,-0.01]), 0, None)
    return (base / base.sum())

def _hash_uniform(s: str) -> float:
    h = hashlib.sha256(s.encode("utf-8")).hexdigest()
    return int(h[:8], 16) / 0xFFFFFFFF

def _pick_by_probs(u: float, probs):
    c = 0.0
    for i, p in enumerate(probs):
        c += float(p)
        if u < c: return i
    return len(probs)-1

def generate_subproduct_dim(
    acquisitions: pd.DataFrame,
    deterministic: bool = True,
    seed: int | None = 42,
    include_rank: bool = True,
) -> pd.DataFrame:
    if not deterministic and seed is not None:
        np.random.seed(seed); random.seed(seed)

    base = (acquisitions[["card_id","card_scheme","product","segment"]]
            .assign(card_id=lambda d: d["card_id"].astype(str).str.strip().str.upper())
            .drop_duplicates("card_id").reset_index(drop=True))

    tiers = np.array(["Classic","Platinum","Signature"])
    rank_map = {"N/A":0,"Classic":1,"Platinum":2,"Signature":3}

    rows = []
    for r in base.itertuples(index=False):
        card_id, scheme, product, segment = r
        if scheme == "mada":
            sub = "N/A"
        else:
            probs = _subproduct_probs(product, segment)
            if deterministic:
                u = _hash_uniform(f"{card_id}")
                idx = _pick_by_probs(u, probs)
            else:
                idx = np.random.choice(len(tiers), p=probs)
            sub = tiers[idx]
        rows.append((card_id, scheme, product, sub))

    df = pd.DataFrame(rows, columns=["card_id","card_scheme","product","subproduct"])
    if include_rank: df["subproduct_rank"] = df["subproduct"].map(rank_map).astype(int)
    return df

def save_subproducts_csv(subproducts: pd.DataFrame, outdir: str = ".") -> str:
    """Сохраняет таблицу subproducts в CSV."""
    outdir = outdir.rstrip("/\\")  # <-- сначала обрезаем вручную
    path = f"{outdir}/subproducts.csv"
    subproducts.to_csv(path, index=False, encoding="utf-8")
    return path
