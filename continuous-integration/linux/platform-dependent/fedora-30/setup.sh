#!/bin/bash

SCRIPT_DIR="$(realpath $(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd) )"

dnf --assumeyes install \
    bsdtar \
    clinfo \
    g++ \
    jq \
    libatomic \
    python3-devel \
    python3-pip \
    wget \
    || exit $?

alternatives --install /usr/bin/python python /usr/bin/python3 0 || exit $?
alternatives --install /usr/bin/pip pip /usr/bin/pip3 0 || exit $?

source $(realpath $SCRIPT_DIR/../common.sh) || exit $?
# Install OpenCL CPU runtime driver prerequisites
dnf --assumeyes install \
    numactl-libs \
    redhat-lsb-core \
    || exit $?
install_opencl_cpu_runtime || exit $?

function install_www_deb {
    TMP_DIR=$(mktemp --tmpdir --directory zivid-python-install-www-deb-XXXX) || exit $?
    pushd $TMP_DIR || exit $?
    wget -nv "$@" || exit $?
    ar x ./*deb || exit $?
    bsdtar -xf data.tar.*z -C / || exit $?
    ldconfig || exit $?
    popd || exit $?
    rm -r $TMP_DIR || exit $?
}

install_www_deb "https://www.zivid.com/hubfs/softwarefiles/releases/${ZIVID_SDK_EXACT_VERSION}/u18/zivid-telicam-driver_${ZIVID_TELICAM_EXACT_VERSION}_amd64.deb" || exit $?
install_www_deb "https://www.zivid.com/hubfs/softwarefiles/releases/${ZIVID_SDK_EXACT_VERSION}/u18/zivid_${ZIVID_SDK_EXACT_VERSION}_amd64.deb" || exit $?