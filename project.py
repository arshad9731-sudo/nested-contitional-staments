import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class AgeValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Range Validator Pro")
        self.root.geometry("550x600")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self.total_checks = 0
        self.success_count = 0
        self.failure_count = 0

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.setup_styles()

        self.create_header()
        self.create_input_frame()
        self.create_stats_frame()
        self.create_log_frame()
        self.create_footer()

        self.root.bind("<Return>", lambda event: self.process_verification())
        self.root.bind("<Escape>", lambda event: self.reset_fields())

    def setup_styles(self):
        self.style.configure(".", background="#1e1e2e", foreground="#cdd6f4")
        self.style.configure("TFrame", background="#1e1e2e")
        self.style.configure("Card.TFrame", background="#252538", borderwidth=1, relief="solid")
        self.style.configure("TLabel", background="#1e1e2e", foreground="#cdd6f4", font=("Segoe UI", 10))
        self.style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground="#cba6f7", background="#1e1e2e")
        self.style.configure("Sub.TLabel", font=("Segoe UI", 9, "italic"), foreground="#a6adc8", background="#1e1e2e")
        self.style.configure("StatTitle.TLabel", font=("Segoe UI", 9, "bold"), foreground="#89b4fa", background="#252538")
        self.style.configure("StatNum.TLabel", font=("Segoe UI", 14, "bold"), foreground="#ffffff", background="#252538")
        self.style.configure("Action.TButton", font=("Segoe UI", 10, "bold"), foreground="#ffffff", background="#11111b", borderwidth=0)
        self.style.map("Action.TButton", background=[("active", "#cba6f7"), ("pressed", "#94e2d5")])
        self.style.configure("Reset.TButton", font=("Segoe UI", 10), foreground="#ffffff", background="#313244", borderwidth=0)
        self.style.map("Reset.TButton", background=[("active", "#f38ba8")])

    def create_header(self):
        header_frame = ttk.Frame(self.root, padding=20)
        header_frame.pack(fill="x")
        title = ttk.Label(header_frame, text="AGE VERIFICATION SYSTEM", style="Header.TLabel")
        title.pack(anchor="w")
        subtitle = ttk.Label(header_frame, text="Enterprise evaluation for target demographic range [10 - 20]", style="Sub.TLabel")
        subtitle.pack(anchor="w", pady=(2, 0))

    def create_input_frame(self):
        input_card = ttk.Frame(self.root, padding=20, style="Card.TFrame")
        input_card.pack(fill="x", padx=20, pady=10)
        entry_label = ttk.Label(input_card, text="Enter Target Age:", font=("Segoe UI", 11, "bold"), background="#252538")
        entry_label.pack(side="left", padx=(0, 10))
        self.age_entry = tk.Entry(input_card, font=("Segoe UI", 12), width=12, bg="#11111b", fg="#cdd6f4", insertbackground="#ffffff", bd=1, relief="solid", justify="center")
        self.age_entry.pack(side="left", padx=5, ipady=4)
        self.age_entry.focus()
        self.verify_btn = ttk.Button(input_card, text="Verify Data", style="Action.TButton", command=self.process_verification)
        self.verify_btn.pack(side="left", padx=15, ipady=2)
        self.reset_btn = ttk.Button(input_card, text="Reset", style="Reset.TButton", command=self.reset_fields)
        self.reset_btn.pack(side="left", padx=5, ipady=2)

    def create_stats_frame(self):
        stats_outer = ttk.Frame(self.root, padding=0)
        stats_outer.pack(fill="x", padx=20, pady=10)
        self.box_total = ttk.Frame(stats_outer, padding=10, style="Card.TFrame")
        self.box_total.pack(side="left", fill="both", expand=True, padx=(0, 5))
        ttk.Label(self.box_total, text="TOTAL CHECKS", style="StatTitle.TLabel").pack()
        self.lbl_stat_total = ttk.Label(self.box_total, text="0", style="StatNum.TLabel")
        self.lbl_stat_total.pack(pady=(5, 0))
        self.box_success = ttk.Frame(stats_outer, padding=10, style="Card.TFrame")
        self.box_success.pack(side="left", fill="both", expand=True, padx=5)
        ttk.Label(self.box_success, text="IN-RANGE (10-20)", style="StatTitle.TLabel", foreground="#a6e3a1").pack()
        self.lbl_stat_success = ttk.Label(self.box_success, text="0", style="StatNum.TLabel")
        self.lbl_stat_success.pack(pady=(5, 0))
        self.box_fail = ttk.Frame(stats_outer, padding=10, style="Card.TFrame")
        self.box_fail.pack(side="left", fill="both", expand=True, padx=(5, 0))
        ttk.Label(self.box_fail, text="OUT OF RANGE / ERR", style="StatTitle.TLabel", foreground="#f38ba8").pack()
        self.lbl_stat_fail = ttk.Label(self.box_fail, text="0", style="StatNum.TLabel")
        self.lbl_stat_fail.pack(pady=(5, 0))

    def create_log_frame(self):
        log_label = ttk.Label(self.root, text="System Transaction Activity Logs:", font=("Segoe UI", 10, "bold"))
        log_label.pack(anchor="w", padx=20, pady=(15, 2))
        log_container = ttk.Frame(self.root, style="Card.TFrame")
        log_container.pack(fill="both", expand=True, padx=20, pady=(0, 10))
        
        # Fixed: Changed font size from 9.5 to integer 10
        self.log_box = tk.Text(log_container, font=("Consolas", 10), bg="#11111b", fg="#a6adc8", bd=0, state="disabled", wrap="word")
        
        scrollbar = ttk.Scrollbar(log_container, orient="vertical", command=self.log_box.yview)
        self.log_box.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.log_box.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.log_box.tag_config("INFO", foreground="#89b4fa")
        
        # Fixed: Changed inline tag font configurations to use integer 10
        self.log_box.tag_config("SUCCESS", foreground="#a6e3a1", font=("Consolas", 10, "bold"))
        self.log_box.tag_config("FAIL", foreground="#f38ba8")
        self.log_box.tag_config("ERROR", foreground="#fab387", font=("Consolas", 10, "underline"))
        
        self.append_log("System initialization completed. Waiting for operational entry matrix...", "INFO")

    def create_footer(self):
        footer = ttk.Frame(self.root, padding=10)
        footer.pack(fill="x", side="bottom")
        lbl_hint = ttk.Label(footer, text="Shortcuts: [Enter] Verify | [Esc] Clear Input Form", style="Sub.TLabel")
        lbl_hint.pack(side="left")
        lbl_ver = ttk.Label(footer, text="v2.1.0 (Stable)", style="Sub.TLabel")
        lbl_ver.pack(side="right")

    def append_log(self, message, tag="INFO"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_line = f"[{timestamp}] [{tag}] {message}\n"
        self.log_box.configure(state="normal")
        self.log_box.insert("end", formatted_line, tag)
        self.log_box.configure(state="disabled")
        self.log_box.see("end")

    def process_verification(self):
        raw_string = self.age_entry.get().strip()
        if not raw_string:
            messagebox.showwarning("Form Verification Deficit", "Target numeric space cannot execute on an empty field submission.")
            return
        try:
            age = int(raw_string)
            self.total_checks += 1
            if age < 0 or age > 125:
                self.failure_count += 1
                self.append_log(f"Rejected valuation entry error: Input [{age}] breaks biological safety bounds boundaries.", "ERROR")
                messagebox.showerror("Biological Constraint Limit Exception", "Value parsed overflows normal parameters (0 - 125 allowed).")
            else:
                # --- Advanced Nested Conditional Structure ---
                if age >= 10:
                    if age <= 20:
                        self.success_count += 1
                        self.append_log(f"Validated Input: Age {age} conforms inside criteria [10-20].", "SUCCESS")
                    else:
                        self.failure_count += 1
                        self.append_log(f"Validation Target Out of Scope: Age {age} failed requirement thresholds (> 20).", "FAIL")
                else:
                    self.failure_count += 1
                    self.append_log(f"Validation Target Out of Scope: Age {age} failed requirement thresholds (< 10).", "FAIL")
        except ValueError:
            self.failure_count += 1
            self.append_log(f"Exception parsing sequence stack: [{raw_string}] is a non-integer token.", "ERROR")
            messagebox.showerror("Data Stream Typing Error", f"Parsing failure on token string values '{raw_string}'. Please submit whole integers.")
        finally:
            self.update_stats_display()

    def update_stats_display(self):
        self.lbl_stat_total.config(text=str(self.total_checks))
        self.lbl_stat_success.config(text=str(self.success_count))
        self.lbl_stat_fail.config(text=str(self.failure_count))

    def reset_fields(self):
        self.age_entry.delete(0, tk.END)
        self.age_entry.focus()
        self.append_log("User reset clear form input values dispatched successfully.", "INFO")

if __name__ == "__main__":
    window_manager = tk.Tk()
    runtime_app = AgeValidatorApp(window_manager)
    window_manager.mainloop()
