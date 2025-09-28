import subprocess, sys, pathlib

def run_script(script, input_path):
    res = subprocess.run(
        [sys.executable, script],
        input=open(input_path, "rb"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return res.stdout.decode().strip()

def test_example_sum_matches_expected(tmp_path):
    root = pathlib.Path(__file__).resolve().parents[1]
    script = str(root / "problems" / "example_sum" / "main.py")
    input_path = str(root / "problems" / "example_sum" / "input1.txt")
    expected_path = root / "problems" / "example_sum" / "output1.txt"
    out = run_script(script, input_path)
    assert out.strip() == expected_path.read_text().strip()
