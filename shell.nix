{ pkgs ? import <nixpkgs> {}}:
with pkgs;
mkShell {
  buildInputs = [
    python310
  ] ++ (with python310Packages; [
    requests
    urllib3
    beautifulsoup4
    lxml
    genanki    
  ]);
}
