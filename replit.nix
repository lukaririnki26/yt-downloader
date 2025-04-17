{ pkgs }: {
  deps = [
    pkgs.python312Full
    pkgs.ffmpeg
    pkgs.libffi
    pkgs.openssl
    pkgs.sqlite
    pkgs.zlib
    pkgs.makeWrapper
    pkgs.git
    pkgs.cacert
    pkgs.python312Packages.pip
    pkgs.python312Packages.setuptools
    pkgs.python312Packages.wheel
  ];
}
