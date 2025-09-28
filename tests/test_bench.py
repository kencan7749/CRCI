import subprocess, sys, pathlib, pytest

@pytest.mark.parametrize("runs", [100])
def test_bench_example_sum(benchmark, runs):
    root = pathlib.Path(__file__).resolve().parents[1]
    script = str(root / "problems" / "example_sum" / "main.py")
    input_path = str(root / "problems" / "example_sum" / "input1.txt")

    def run_once():
        subprocess.run([sys.executable, script],
                       input=open(input_path, "rb").read(),
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       check=True)

    benchmark.pedantic(run_once, rounds=runs, iterations=1)
