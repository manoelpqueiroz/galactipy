from hooks.pre_gen_project import (
    MAX_USERNAME_LENGTH,
    MIN_USERNAME_LENGTH,
    RESERVED_PROJECTS,
    RESERVED_USERNAMES,
    validate_package_name,
    validate_repo_name,
    validate_semver,
    validate_username,
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

    assert validate_repo_name(valid_slug, RESERVED_PROJECTS) is None


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
    ],
)
def test_invalid_repo_names(invalid_slug):

    with pytest.raises(ValueError):
        validate_repo_name(invalid_slug, RESERVED_PROJECTS)


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
        validate_repo_name(invalid_slug, RESERVED_PROJECTS)


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

    assert validate_package_name(valid_package) is None


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
        "jFC1",
        "NHKs",
        "DAc9_",
        "h0CKQF",
        "s_nGo7mR6",
        "@4cjsO#VB3jn",
    ],
)
def test_invalid_package_names(invalid_package):

    with pytest.raises(ValueError):
        validate_package_name(invalid_package)


@pytest.mark.parametrize(
    "valid_username",
    [
        "15SV",
        "vIOh",
        "jO5Obrfq6aR8b",
        "t5cfEsgM3hhV90",
        "GKeYlsUOT",
        "75e6R",
        "VgCaS7mOIzikWJJ",
        "K-fpQC",
        "A-zn-ET-K-k-k-3I",
        "MvkWGKFKj-qRFT",
    ],
)
def test_valid_usernames(valid_username):

    assert validate_username(valid_username, RESERVED_USERNAMES) is None


@pytest.mark.parametrize(
    "invalid_username",
    [
        "robots.txt",
        "groups",
        "500.html",
        "v2",
        "projects",
        "7w--StBkn8Pk5s",
        "7wezIt1ets-",
        "-sxSfLvkK",
        "b--5DLF--hueyK3G",
        "Y9ih5!!SjHPus",
        "!HXk8A",
        "c@N9hPPCWoronAm",
        "OL+UjzQ_C.Z",
        "Af8.uH",
        "Go!b",
        "#4FeBLTCDd@",
        "dhsqWL/d",
    ],
)
def test_invalid_usernames(invalid_username):

    with pytest.raises(ValueError):
        validate_username(invalid_username, RESERVED_USERNAMES)


def test_username_length():

    string = "a"

    for n in range(260):
        username = string * n

        if MIN_USERNAME_LENGTH <= n <= MAX_USERNAME_LENGTH:
            assert validate_username(username, RESERVED_USERNAMES) is None
        else:
            with pytest.raises(ValueError):
                validate_username(username, RESERVED_USERNAMES)


@pytest.mark.parametrize(
    "valid_semver",
    [
        "170.0.12-alpha-00-b73ts",
        "1.8.5+build-7.8.9",
        "0.0.0+b",
        "100.0.0-0.0.0+0.0.0-0.0.0",
        "170.0.1-0b97-07-b",
        "4823.8585.846133-alpha+rc.uu.723-lpt.13",
    ],
)
def test_valid_semver(valid_semver):

    assert validate_semver(valid_semver) is None


@pytest.mark.parametrize(
    "invalid_semver",
    [
        "00.0.0",
        "0.00.0",
        "0.0.00",
        "00.00.00",
        "01.0.0",
        "0.02.0",
        "0.0.06",
        "07.08.09",
        "1.2.3-",
        "1.2.3-01",
        "1.2.3-13b7.01",
        "1.2.3-7_beta",
        "1.2.3-alpha.68+pre..test",
        "1.2.3-0b00+t.549.000.tst.",
    ],
)
def test_invalid_semvers(invalid_semver):

    with pytest.raises(ValueError):
        validate_semver(invalid_semver)
