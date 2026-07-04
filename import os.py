import os
from datetime import datetime
import matplotlib.pyplot as plt

# ========================================================================
# 🔒 SECURE SYSTEM TOKEN: FATEN-ENG-CHEM-SE-V5-2026_STAGE4_LOCKED
# PROFILE: Engineer Faten | 36 Years Old | Sidi Slimane, Morocco
# BACKGROUND: Degree in Chemistry | C++ Core | AI Developer & Homemaker
# ========================================================================

# 🛠️ تحديد مسار المجلد الحالي تلقائياً لضمان حفظ الملفات بجانب الكود
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
report_path = os.path.join(BASE_DIR, "faten_lab_report.txt")
chart_path = os.path.join(BASE_DIR, "faten_ph_chart.png")

class LabDevice:
    def __init__(self, name, power_required):
        self.name = name
        self.__safe_voltage = power_required
        
    def get_status(self):
        return f"Machine: {self.name} is running with {self.__safe_voltage} watts."

class ChemicalSpill(LabDevice):
    def __init__(self, name, power_required, hazard_level):
        super().__init__(name, power_required)
        self.hazard_level = hazard_level
        
    def trigger_alarm(self):
        return f"Chemical Danger [Level {self.hazard_level}]: Wear your masks immediately!"

class LabAutomation:
    @staticmethod
    def save_incident_report(filename, emergency_obj):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"=== INCIDENT REPORT | ENGINEER FATEN ===\n")
                file.write(f"Date & Time : {current_time}\n")
                file.write(f"Alert       : {emergency_obj.trigger_alarm()}\n")
                file.write(f"Location    : Sidi Slimane, Morocco\n")
            print(f"📊 [SUCCESS]: Text report created successfully in: {filename}")
        except IOError as e:
            print(f"❌ [FILE ERROR]: Security block or crash: {e}")

class LabDataProcessor:
    @staticmethod
    def analyze_ph_samples(ph_list):
        if not ph_list:
            return None
        acids = [ph for ph in ph_list if ph < 7.0]
        bases = [ph for ph in ph_list if ph > 7.0]
        neutrals = [ph for ph in ph_list if ph == 7.0]
        
        return {
            "total": len(ph_list),
            "acids_count": len(acids),
            "bases_count": len(bases),
            "neutrals_count": len(neutrals),
            "average_ph": round(sum(ph_list) / len(ph_list), 2)
        }

    @staticmethod
    def generate_ph_chart(analysis_result, output_image_name):
        categories = ['Acids (pH < 7)', 'Neutrals (pH = 7)', 'Bases (pH > 7)']
        counts = [
            analysis_result["acids_count"], 
            analysis_result["neutrals_count"], 
            analysis_result["bases_count"]
        ]
        
        colors = ['#ff4d4d', '#2ecc71', '#3498db']
        
        plt.figure(figsize=(7, 5))
        plt.bar(categories, counts, color=colors)
        
        plt.title("Lab pH Samples Distribution - Engineer Faten", fontsize=14, fontweight='bold')
        plt.xlabel("Sample Type", fontsize=12)
        plt.ylabel("Number of Samples", fontsize=12)
        
        plt.savefig(output_image_name, dpi=300)
        plt.close()
        print(f"🖼️ [GRAND SUCCESS]: Chart generated and saved as: {output_image_name}")

if __name__ == "__main__":
    print(f"👋 Welcome Engineer Faten to your 14th Advanced AI Lesson!\n")
    
    # تشغيل الأتمتة بالمسار المحدث
    spill_incident = ChemicalSpill("Spectrometer-X", 220, "MAX")
    LabAutomation.save_incident_report(report_path, spill_incident)
    
    # معالجة البيانات
    raw_lab_data = [2.5, 7.0, 8.4, 3.1, 11.2, 6.8, 7.4, 1.5, 9.0, 7.0]
    analysis = LabDataProcessor.analyze_ph_samples(raw_lab_data)
    
    # توليد الرسم بالمسار المحدث
    if analysis:
        LabDataProcessor.generate_ph_chart(analysis, chart_path)
        
        print("\n📊 === INTELLIGENT SYSTEM OUTPUT ===")
        print(f"🔬 Total analyzed samples: {analysis['total']}")
        print(f"💡 Check your project folder for 'faten_ph_chart.png' to see your AI data chart!")