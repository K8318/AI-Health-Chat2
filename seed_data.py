from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Doctor, Medicine

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed the database with sample doctors, medicines, and an admin user'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding database...')

        # Admin user
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin', email='admin@medibot.com',
                password='admin123', role='admin',
                first_name='Admin', last_name='User'
            )
            self.stdout.write('  ✅ Admin user created (username: admin, password: admin123)')

        # Sample patient
        if not User.objects.filter(username='patient1').exists():
            User.objects.create_user(
                username='patient1', email='patient@medibot.com',
                password='patient123', role='patient',
                first_name='John', last_name='Doe',
                blood_group='O+', phone='555-0100'
            )
            self.stdout.write('  ✅ Sample patient created (username: patient1, password: patient123)')

        # Doctors
        doctors_data = [
            ('Sarah Johnson', 'General Physician', 'City Medical Center', '555-0201', 12, 4.8),
            ('Michael Chen', 'Cardiologist', 'Heart & Vascular Institute', '555-0202', 18, 4.9),
            ('Priya Patel', 'Dermatologist', 'Skin Care Clinic', '555-0203', 8, 4.7),
            ('James Wilson', 'Neurologist', 'NeuroHealth Hospital', '555-0204', 15, 4.8),
            ('Maria Garcia', 'Pediatrician', 'Children\'s Health Center', '555-0205', 10, 4.9),
            ('David Kim', 'Orthopedic', 'Bone & Joint Clinic', '555-0206', 14, 4.6),
            ('Emily Brown', 'Psychiatrist', 'Mind Wellness Center', '555-0207', 9, 4.7),
            ('Robert Singh', 'Gastroenterologist', 'Digestive Health Clinic', '555-0208', 11, 4.5),
            ('Lisa Wang', 'Gynecologist', 'Women\'s Health Center', '555-0209', 13, 4.8),
            ('Thomas Lee', 'ENT Specialist', 'Ear Nose Throat Clinic', '555-0210', 7, 4.6),
            ('Aisha Mohammed', 'Ophthalmologist', 'Eye Care Institute', '555-0211', 10, 4.7),
            ('Carlos Rivera', 'Pulmonologist', 'Lung Health Center', '555-0212', 16, 4.8),
            ('Nina Patel', 'Endocrinologist', 'Diabetes & Hormone Clinic', '555-0213', 12, 4.7),
        ]
        count = 0
        for name, spec, hospital, phone, exp, rating in doctors_data:
            _, created = Doctor.objects.get_or_create(
                name=name,
                defaults={
                    'specialization': spec, 'hospital': hospital,
                    'phone': phone, 'experience_years': exp,
                    'rating': rating, 'is_available': True,
                    'available_days': 'Mon-Fri', 'available_time': '9AM - 5PM',
                }
            )
            if created:
                count += 1
        self.stdout.write(f'  ✅ {count} doctors created')

        # Medicines
        medicines_data = [
            ('Paracetamol', 'Acetaminophen', 'Painkiller', 'Used to relieve mild to moderate pain and reduce fever.', '500mg every 4-6 hours', 'Nausea, rash (rare)', 'Do not exceed 4g/day. Avoid with alcohol.', False),
            ('Ibuprofen', 'Ibuprofen', 'Painkiller', 'Anti-inflammatory used for pain, fever, and inflammation.', '400mg every 6-8 hours with food', 'Stomach upset, headache', 'Avoid if you have kidney disease or ulcers.', False),
            ('Amoxicillin', 'Amoxicillin', 'Antibiotic', 'Broad-spectrum antibiotic for bacterial infections.', '500mg three times daily', 'Diarrhea, nausea, rash', 'Complete full course. Allergic to penicillin? Avoid.', True),
            ('Cetirizine', 'Cetirizine HCl', 'Antihistamine', 'Relieves symptoms of allergies and hay fever.', '10mg once daily', 'Drowsiness, dry mouth', 'May cause drowsiness. Avoid driving.', False),
            ('Omeprazole', 'Omeprazole', 'Antacid', 'Reduces stomach acid production. Used for GERD and ulcers.', '20mg once daily before meals', 'Headache, diarrhea', 'Long-term use: consult doctor.', False),
            ('Loratadine', 'Loratadine', 'Antihistamine', 'Non-drowsy antihistamine for allergies and hives.', '10mg once daily', 'Headache, dry mouth', 'Safe for most adults.', False),
            ('Metformin', 'Metformin HCl', 'Diabetes', 'Controls blood sugar levels in Type 2 diabetes.', '500mg twice daily with meals', 'Nausea, diarrhea, stomach pain', 'Monitor kidney function. Not for Type 1 diabetes.', True),
            ('Atorvastatin', 'Atorvastatin', 'Cardiovascular', 'Lowers cholesterol and reduces cardiovascular risk.', '10-80mg once daily', 'Muscle pain, liver enzyme changes', 'Avoid grapefruit juice. Regular liver tests needed.', True),
            ('Salbutamol', 'Albuterol', 'Respiratory', 'Relieves bronchospasm in asthma and COPD.', '1-2 puffs every 4-6 hours as needed', 'Tremor, fast heartbeat', 'Seek emergency help if no relief after 2 puffs.', True),
            ('Vitamin C', 'Ascorbic Acid', 'Vitamins', 'Boosts immunity, antioxidant, supports wound healing.', '500-1000mg daily', 'Stomach upset at high doses', 'Very safe. Excess excreted in urine.', False),
            ('Vitamin D3', 'Cholecalciferol', 'Vitamins', 'Essential for bone health, immunity, and mood.', '1000-2000 IU daily', 'Nausea at very high doses', 'Avoid very high doses without testing.', False),
            ('Antacid Syrup', 'Aluminum Hydroxide', 'Antacid', 'Fast relief from heartburn and acid indigestion.', '10ml three times daily after meals', 'Constipation', 'Do not take with other medicines simultaneously.', False),
            ('Fluconazole', 'Fluconazole', 'Antifungal', 'Treats fungal infections including yeast infections.', '150mg single dose (or as directed)', 'Headache, nausea', 'Drug interactions possible. Consult pharmacist.', True),
            ('Sertraline', 'Sertraline HCl', 'Antidepressant', 'Treats depression, anxiety, OCD, and PTSD.', '50-200mg once daily', 'Nausea, insomnia, sexual dysfunction', 'Do not stop abruptly. Takes 2-4 weeks to work.', True),
            ('ORS Powder', 'Oral Rehydration Salts', 'Other', 'Replaces fluids and electrolytes lost due to diarrhea.', '1 sachet in 1L water, sip frequently', 'None at normal doses', 'Use fresh solution within 24 hours.', False),
        ]
        med_count = 0
        for name, generic, cat, desc, dosage, side, warn, rx in medicines_data:
            _, created = Medicine.objects.get_or_create(
                name=name,
                defaults={
                    'generic_name': generic, 'category': cat, 'description': desc,
                    'dosage': dosage, 'side_effects': side, 'warnings': warn,
                    'prescription_required': rx,
                }
            )
            if created:
                med_count += 1
        self.stdout.write(f'  ✅ {med_count} medicines created')
        self.stdout.write(self.style.SUCCESS('\n🎉 Database seeded successfully!\n'))
        self.stdout.write('  Login credentials:')
        self.stdout.write('  👤 Admin   → username: admin    | password: admin123')
        self.stdout.write('  👤 Patient → username: patient1 | password: patient123')
