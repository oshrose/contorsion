def test_small_molecule_torsion_scan(tmp_path):

    # Run a torsion scan
    result = run_torsion_scan(
        input_file="tests/data/small_molecule.xyz",
        output_dir=tmp_path
    )

    # Check that it completed
    assert result is not None

    # Check that expected output exists
    assert (tmp_path / "torsion_scan.csv").exists()

    # Check that the output contains results
    assert len(read_torsion_scan(tmp_path)) > 0


contorsion run-reference-scans \
     "CCO" \
     --method small \
     --program mace \
     --output-dir reference_scans \
     --grid-spacing 15 \
     --ncores 4 \
