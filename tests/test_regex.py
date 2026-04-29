from hooks.pre_gen_project import (
    MAX_NAMESPACE_LENGTH,
    MIN_NAMESPACE_LENGTH,
    validate_email_address,
    validate_namespace,
    validate_package_name,
    validate_repo_name,
)

import pytest


@pytest.mark.parametrize(
    "valid_slug",
    [
        "9zUZCqQAOP1NjAgU",
        "o3fYbfg2kMjJjQd3DHKPnbp",
        "vBmu8T8MGL",
        "Odcp6pqK2Y4I.PKIZ0WfbZj",
        "rQV.SgJhbsy.n7GhitwpnM_rN",
        "9SwPJgigH",
        "Kn7E2vsji1",
        "BgaoXUu.gJxBDpLV",
        "AjgB",
        "WCdj7Ii6sZUtCxIeBGh1",
        "nVB2",
        "B7cOcPkOYo9nF0-jlaLqYoK3",
        "f07gwCbWZK-prBg",
        "WxCKHO-TpiyP",
        "4kc_xSi",
        "HnH1-K5Cj2GtdG3wnNM6V",
        "JUr.xHPsKW5pc_MhZiSEp",
        "65cY_A71B3GgaYrw68a",
        "MhD-k5p",
        "MGA0xNXL8PHIOEnD",
        "BsX-ZRfSIr-c0yDl",
        "hs7caUTKZNo",
        "BS7l1HUDL3R7tpqqsYw",
        "feC5BkNT8.SvRDpI.0",
        "ZtwAd3cwEF",
        "mpf6",
        "lly31685PEyWLngr",
        "cltK.gti",
        "1HRIiu0YhWfkDy37Fj9Xdmv.gt",
        "FBa_vC07MB2Ib.gi",
        "JdUzsPiRbNs9tN02kXgJglQ.it",
        "li.fF_git",
        "gziUigB-git",
        "dK0Ry9KAW934afvdmyY.atmo",
        "bP4xRFjShWp1kFn.tom",
        "Kf0h2hIn-zG0JlrJ7JZT.aom",
        "s_5mA_mlQZfSYwyT0O5h3GN.atm",
        "jaXXN-toaAboZ2szbOW-mTQ.ato",
        "8DcrvdJB4C3O30g1xlHTbypj_atom",
        "ChK4ASrqjt_0G-atom",
    ],
)
def test_valid_repo_names(valid_slug):
    assert validate_repo_name(valid_slug) is None  # type: ignore[func-returns-value]


@pytest.mark.parametrize(
    "invalid_slug",
    [
        r"\-",
        "badges",
        "blame",
        "blob",
        "builds",
        "commits",
        "create",
        "create_dir",
        "edit",
        "environments/folders",
        "files",
        "find_file",
        "gitlab-lfs/objects",
        "info/lfs/objects",
        "new",
        "preview",
        "raw",
        "refs",
        "tree",
        "update",
        "wikis",
        ".XGiovqokdpk30Sc+S",
        "-dtPTEHNDy1o",
        "_9LMkzhMIV6FwZ",
        "Prc9OVWpQJOn+",
        "JEWF2BDkg.",
        "MeCvP0U1wxRxjLFgfSZ5-",
        "JEUcDGf_",
        "aaJslw..vJ0wgGtJIF",
        "ywt0--zdgE",
        "1xmGB3qn__71TxSnXZKywl3TK",
        "fgks-_EOgiGHjQ5",
        "4WLLRG-4h8_-B1F_3WEc",
        "lZ._V.sGfZz5qCiR2",
        "d1_.NU9BHcCW1",
        "3a-.9w",
        "O1rEaP2.-sD",
        "bPcH@ARcZ",
        "e+Qj",
        "A7dSDs*8Ug",
        "4UnB#Se4dJ4",
        "OY_O3KjBLZ;KJ-hpvjox/Dveg2",
        "t0bmh!sj55",
        "tGcyDjUQoZ-ecMuyUCiFVd.git",
        "cFLtG.4Q0lty8vNjMew1kef.atom",
        "_somerepo",
    ],
)
def test_invalid_repo_names(invalid_slug):
    with pytest.raises(ValueError):
        validate_repo_name(invalid_slug)


@pytest.mark.parametrize(
    "invalid_slug",
    [
        "+fit9YR",
        "/Xcpjw8jkjHZH2X",
        "@PigZnNND",
        "NWQX9PL5mF+",
        "xKc3YrKCVNOahZeGvIQH31ye!",
        "kci2h2GC0P2MzlCjUyzcx#",
        ".gczpb.",
        "-UtE6tqfvAqC8iltmgIu-",
        "_JJeUvmIGQy_",
        ".SOXJ6_",
        "-izVxmqfqc6XsTqDnQ5Cy6uk.",
        "2MeqULP...wK5vbUZovmkeL6mL",
        "ctfwycYR6AUs---NDEl",
        "WsA___YVYYdPb1hf57Z",
        "umVbUkERv++nPYbWJXTD7",
        "q7JB@@v8yZpYanxDSkHzhXy",
        "1OXPt**Y",
        "1AM7Kbp63OEU##mEwYHRTKtk",
        "gxiho8L..git",
        "3Z1ORQzFftL9xqa-.atom",
    ],
)
def test_doubly_invalid_repo_names(invalid_slug):
    with pytest.raises(ValueError):
        validate_repo_name(invalid_slug)


@pytest.mark.parametrize(
    "valid_package",
    [
        "uqp0w",
        "odjl5igrx",
        "naqntv",
        "zd9lwp9",
        "ul6w25ra8",
        "tp7",
        "qwtokmypv",
        "b538efggk_t6h7",
        "isifkzsot4q6ikq",
        "ffvd9iqnj63",
        "qvpfy13ia1d18",
        "krsrlo8zvhc9",
        "pq_bqb",
        "em_g6_rqq_e5",
        "s95__eas33",
    ],
)
def test_valid_package_names(valid_package):
    assert validate_package_name(valid_package) is None  # type: ignore[func-returns-value]


@pytest.mark.parametrize(
    "invalid_package",
    [
        "6iig7ot",
        "-oxclb3f",
        "l!kzh76wq1uq-",
        "+!ro-9_@",
        "813ddy/zosoq8h",
        "-6#p66",
        "61txxnrpi#1x7",
        "g9hzu1ia_",
        "sysfeq.ywbw",
        "jFC1_",
        "_NHKs",
        "DAc9_",
        "h0C.KQF",
        "s_nGo7mR6.",
        "@4cjsO#VB3jn",
        "_somerepo",
        "await",
        "return",
        "nonlocal",
    ],
)
def test_invalid_package_names(invalid_package):
    with pytest.raises(ValueError):
        validate_package_name(invalid_package)


@pytest.mark.parametrize(
    ("valid_namespace", "platform"),
    [
        ("15SV", "gitlab"),
        ("vIOh", "gitlab"),
        ("jO5Obrfq6aR8b", "gitlab"),
        ("t5cfEsgM3hhV90", "gitlab"),
        ("GKeYlsUOT", "gitlab"),
        ("75e6R", "gitlab"),
        ("VgCaS7mOIzikWJJ", "gitlab"),
        ("K-fpQC", "gitlab"),
        ("A-zn-ET-K-k-k-3I", "gitlab"),
        ("MvkWGKFKj-qRFT", "gitlab"),
        ("15SV", "github"),
        ("vIOh", "github"),
        ("jO5Obrfq6aR8b", "github"),
        ("t5cfEsgM3hhV90", "github"),
        ("GKeYlsUOT", "github"),
        ("75e6R", "github"),
        ("VgCaS7mOIzikWJJ", "github"),
        ("K-fpQC", "github"),
        ("A-zn-ET-K-k-k-3I", "github"),
        ("MvkWGKFKj-qRFT", "github"),
    ],
)
def test_valid_namespaces(valid_namespace, platform):
    assert validate_namespace(valid_namespace, platform) is None  # type: ignore[func-returns-value]


@pytest.mark.parametrize(
    "valid_namespace", ["alpha/beta/gaga", "nested/structures/valid/for/platform"]
)
def test_valid_gitlab_namespaces(valid_namespace):
    assert validate_namespace(valid_namespace, "gitlab") is None  # type: ignore[func-returns-value]


@pytest.mark.parametrize(
    ("invalid_namespace", "platform"),
    [
        ("robots.txt", "gitlab"),
        ("groups", "gitlab"),
        ("500.html", "gitlab"),
        ("v2", "gitlab"),
        ("projects", "gitlab"),
        ("7w--StBkn8Pk5s", "gitlab"),
        ("7wezIt1ets-", "gitlab"),
        ("-sxSfLvkK", "gitlab"),
        ("b--5DLF--hueyK3G", "gitlab"),
        ("Y9ih5!!SjHPus", "gitlab"),
        ("!HXk8A", "gitlab"),
        ("c@N9hPPCWoronAm", "gitlab"),
        ("OL+UjzQ_C.Z", "gitlab"),
        ("Af8.uH", "gitlab"),
        ("Go!b", "gitlab"),
        ("#4FeBLTCDd@", "gitlab"),
        ("dhsqWL/d", "gitlab"),
        ("alpha/projects/groups", "gitlab"),
        (
            (
                "one/two/three/four/five/six/seven/eight/nine/ten/eleven/twelve/"
                "thirteen/fourteen/fifteen/sixteen/seventeen/eighteen/nineteen/twenty/"
                "twentyone"
            ),
            "gitlab",
        ),
        ("robots.txt", "github"),
        ("groups", "github"),
        ("500.html", "github"),
        ("v2", "github"),
        ("projects", "github"),
        ("7w--StBkn8Pk5s", "github"),
        ("7wezIt1ets-", "github"),
        ("-sxSfLvkK", "github"),
        ("b--5DLF--hueyK3G", "github"),
        ("Y9ih5!!SjHPus", "github"),
        ("!HXk8A", "github"),
        ("c@N9hPPCWoronAm", "github"),
        ("OL+UjzQ_C.Z", "github"),
        ("Af8.uH", "github"),
        ("Go!b", "github"),
        ("#4FeBLTCDd@", "github"),
        ("dhsqWL/d", "github"),
        ("alpha/projects/groups", "github"),
    ],
)
def test_invalid_namespaces(invalid_namespace, platform):
    with pytest.raises(ValueError):
        validate_namespace(invalid_namespace, platform)


@pytest.mark.parametrize(
    "valid_email",
    [
        "something@google.com",
        "=wild+suff@skills.md.ar",
        "___still/valid@ultra-secret.society",
        "helluva#box@number09.after005.expect-this.io",
        "==kawaii==@district.090.end7",
    ],
)
def test_valid_emails(valid_email):
    assert validate_email_address(valid_email) is None  # type: ignore[func-returns-value]


@pytest.mark.parametrize(
    "invalid_email",
    [
        "@start@does.not.compile",
        "starts=good@but.does.not.end.well#",
        "even-with#dashes@you.cant.end-",
        "so...you-re-telling#me@periods.cant.be.stacked",
        "hey@underscore_domains_dont_exist.com",
    ],
)
def test_invalid_emails(invalid_email):
    with pytest.raises(ValueError):
        validate_email_address(invalid_email)


@pytest.mark.parametrize("platform", ["gitlab", "github"])
def test_username_length(platform):
    string = "a"

    for n in range(260):
        username = string * n

        if MIN_NAMESPACE_LENGTH <= n <= MAX_NAMESPACE_LENGTH:
            assert validate_namespace(username, platform) is None  # type: ignore[func-returns-value]
        else:
            with pytest.raises(ValueError):
                validate_namespace(username, platform)
