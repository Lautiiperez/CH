from django.test import TestCase
from django.utils import timezone
from .models import Medico, Paciente, Cita

class MedicoModelTest(TestCase):
    def setUp(self):
        self.medico = Medico.objects.create(nombre="Dr. John Doe", especialidad="Cardiología")

    def test_medico_creation(self):
        """Verifica que un médico se puede crear correctamente."""
        self.assertTrue(isinstance(self.medico, Medico))
        self.assertEqual(str(self.medico), "Dr. John Doe")  # Usamos str() para obtener el string representation del objeto

class PacienteModelTest(TestCase):
    def setUp(self):
        self.paciente = Paciente.objects.create(nombre="Jane Doe", fecha_nacimiento=timezone.now())

    def test_paciente_creation(self):
        """Verifica que un paciente se puede crear correctamente."""
        self.assertTrue(isinstance(self.paciente, Paciente))
        self.assertEqual(str(self.paciente), "Jane Doe")  # Usamos str() para obtener el string representation del objeto

class CitaModelTest(TestCase):
    def setUp(self):
        self.medico = Medico.objects.create(nombre="Dr. Jane Smith", especialidad="Oncología")
        self.paciente = Paciente.objects.create(nombre="John Smith", fecha_nacimiento=timezone.now())
        self.cita = Cita.objects.create(paciente=self.paciente, medico=self.medico, fecha=timezone.now(), motivo="Consulta regular")

    def test_cita_creation(self):
        """Verifica que una cita se puede crear correctamente."""
        self.assertTrue(isinstance(self.cita, Cita))
        self.assertEqual(str(self.cita), f"Cita de {self.paciente.nombre} con {self.medico.nombre}")  # Usamos str() para obtener el string representation del objeto

    def test_cita_medico_y_paciente(self):
        """Verifica que la cita está asociada al médico y al paciente correctos."""
        self.assertEqual(self.cita.paciente, self.paciente)
        self.assertEqual(self.cita.medico, self.medico)