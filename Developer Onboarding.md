
```markdown
# LodgeiT Global: Developer Onboarding & Local Environment Verification

Welcome to the LodgeiT Global Neurosemantic Engine. This system is a hybrid architecture utilizing Python, SWI-Prolog, and a strict Standard Business Reporting Model (SBRM) ontology backed by GitOps cryptography.

Before contributing to the logic or the UI, every developer must execute this 4-phase verification sequence to ensure their local environment is properly configured and cryptographically sound.

## Phase 1: Verify Ontological Integrity
Our SBRM nodes are stored as Markdown files with YAML frontmatter. We use a Python gatekeeper to ensure no "Truth Decay" (hallucinations or unauthorized edits) has occurred.

1. Open your terminal in the repository root.
2. Run the neurosemantic gatekeeper:
   `python audit_ontology_v2.py`
3. **Expected Output:** `Audit Complete. Passed: 52 | Ignored (Docs): 13 | Quarantined: 0`
   *(Do not proceed if any files are quarantined).*

## Phase 2: Verify Raw Prolog Inference
Prove the core SWI-Prolog engine can natively cross-reference the SBRM ontology, validate accounting equations, and execute jurisdictional tax rules.

1. Launch SWI-Prolog from the terminal:
   `swipl`
2. Load the base domains:
   `['02_Rules/gst_tax_rules.pl', '02_Rules/sbrm_kb.pl'].`

**Test A: Master SBRM Health Checks**
Validate that the core accounting principles hold true across the current state.
3. Run the dashboard command:
   `run_health_checks.`
4. **Expected Output:**
   ```text
   =========================================
           SBRM HEALTH CHECK REPORT         
   =========================================
   [PASS] Accounting Equation (A = L + E)
   [PASS] Asset Rollup (CA + NCA = TA)
   [PASS] Net Profit (Revenue - Expenses = P&L)
   [PASS] Revenue Breakdown (Sum of slices = Total)
   =========================================
   true.

```

**Test B: Multidimensional Branch Reasoner**
Verify the engine can dynamically traverse the SBRM hierarchy. (Note: Sub-branches will not print in raw Prolog as the edge data is dynamically injected by Python later, but the root nodes must resolve without error).
5. Run the four master branch queries:
`generate_branch_structure('urn:uuid:def-sbr-total-assets', 0).`
`generate_branch_structure('urn:uuid:def-sbr-total-liabilities', 0).`
`generate_branch_structure('urn:uuid:def-sbr-total-equity', 0).`
`generate_branch_structure('urn:uuid:def-sbr-profit-loss', 0).`
6. **Expected Output:** Each command should output its respective root node (e.g., `-> urn:uuid:def-sbr-total-assets`) followed immediately by `true.`

**Test C: Jurisdictional Tax Inference**
Prove the engine can cross the SBRM boundary into local tax rules (ATO).
7. Execute the IAWO query:
`calculate_iawo_deduction('urn:uuid:def-sbrm-reporting-entity', 'urn:uuid:def-sbrm-reporting-period-2026', Deduction).`
8. **Expected Output:** `Deduction = 1.0e+05.`

9. Exit Prolog: `halt.`

## Phase 3: Verify the Stateless Python Wrapper & L402 Paywall

We do not fuse Prolog directly into long-running Python memory. We use stateless subprocesses governed by an L402 (Lightning Network) protocol.

1. Run the test desktop GUI:
`python prolog_app.py`
2. Click **"Pay 50 Sats & Calculate IAWO"**.
3. **Expected Output:** The GUI console should display `L402 Validated` followed by `Approved IAWO Deduction: $1.0e+05`.

## Phase 4: Verify the Visual Web Graph

Verify the frontend Streamlit dashboard can parse the JSON-LD export and render the multidimensional SBRM hierarchies.

1. Run the web dashboard:
`streamlit run App.py`
2. **Expected Output:** A local web browser will open displaying the ClientRelay SBRM Dashboard, including the hierarchical Balance Sheet, P&L tabs, and the green Multidimensional Integrity Reasoner checks.

---

**Note on Git Hooks:** This repository enforces a strict pre-commit hook (`.git/hooks/pre-commit`). If you attempt to commit a malformed SBRM node, the commit will be automatically aborted.

```

This makes your onboarding document a bulletproof reflection of the exact capabilities of the engine. Once you've saved this, your foundation is unequivocally complete! Ready for the new thread?

```