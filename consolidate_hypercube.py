import os
import yaml

DIR = './01_Ontology'

def read_val(filename):
    """Safely extracts the numerical magnitude from an SBRM node."""
    path = os.path.join(DIR, filename)
    if not os.path.exists(path): return 0.0
    with open(path, 'r', encoding='utf-8') as f:
        parts = f.read().split('---', 2)
        if len(parts) >= 3:
            return float(yaml.safe_load(parts[1]).get('value', 0.0))
    return 0.0

def update_val(filename, new_val):
    """Injects the consolidated roll-up magnitude back into the Master node."""
    path = os.path.join(DIR, filename)
    if not os.path.exists(path): return
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    parts = content.split('---', 2)
    if len(parts) < 3: return
    
    fm = yaml.safe_load(parts[1])
    fm['value'] = new_val
    new_yaml = yaml.dump(fm, sort_keys=False)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"---\n{new_yaml}---\n{parts[2]}")
    print(f"[CONSOLIDATED] {filename} -> {new_val}")

def consolidate():
    print("=== INITIATING NEUROSEMANTIC CONSOLIDATION ===")
    
    # Leaves: Merging Original Seed with Uplifted CSV Nodes
    cash_base = 50000.0 # Original ledger
    cash_up = read_val('fact-uplift-cash-at-bank-2026.md')
    ar_up = read_val('fact-uplift-accounts-receivable-2026.md')
    nab_up = read_val('fact-uplift-nab-5510-2026.md')
    
    plant = read_val('fact-plant-at-cost-2026.md')
    acc_dep = read_val('fact-accumulated-depreciation-2026.md')
    
    curr_liab_base = 30000.0 # Original AP equivalent
    ap_up = read_val('fact-uplift-accounts-payable-2026.md')
    non_curr_liab = read_val('fact-non-current-liabilities-2026.md')
    
    open_eq = read_val('fact-opening-equity-2025.md')
    cap_intro = read_val('fact-uplift-capital-introduced-2026.md')
    ret_earn = read_val('fact-uplift-retained-earnings-2026.md')
    div_paid = read_val('fact-dividends-paid-2026.md')
    
    rev_base = 100000.0 
    rev_up = read_val('fact-uplift-sales-revenue-2026.md')
    
    exp_base = 80000.0 
    exp_up = read_val('fact-uplift-operating-expenses-2026.md')
    
    # 3D Mathematics Execution
    curr_assets = cash_base + cash_up + ar_up + nab_up
    non_curr_assets = plant - acc_dep
    total_assets = curr_assets + non_curr_assets
    
    curr_liab = curr_liab_base + ap_up
    total_liab = curr_liab + non_curr_liab
    
    total_rev = rev_base + rev_up
    total_exp = exp_base + exp_up
    profit_loss = total_rev - total_exp
    
    total_eq = open_eq + cap_intro + ret_earn + profit_loss - div_paid
    
    # Overwrite Master Nodes
    update_val('fact-current-assets-2026.md', curr_assets)
    update_val('fact-total-assets-2026.md', total_assets)
    update_val('fact-current-liabilities-2026.md', curr_liab)
    update_val('fact-total-liabilities-2026.md', total_liab)
    update_val('fact-revenue-2026.md', total_rev)
    update_val('fact-expenses-2026.md', total_exp)
    update_val('fact-profit-loss-2026.md', profit_loss)
    update_val('fact-total-equity-2026.md', total_eq)
    
    print("=== SYNCHRONIZATION COMPLETE ===")

if __name__ == '__main__':
    consolidate()