from django.test import TestCase
from django.utils import timezone
from gestionClinica.models import Medico, Paciente, Cita

class MedicoModelTest(TestCase):
    """
    Pruebas para el modelo Medico.
    Verifica la creación y representación del objeto Medico.
    """
    def setUp(self):
        self.medico = Medico.objects.create(nombre="Dr. John Doe", especialidad="Cardiología")

    def test_medico_creation(self):
        """Verifica que un médico se puede crear correctamente."""
        self.assertTrue(isinstance(self.medico, Medico))
        self.assertEqual(str(self.medico), "Dr. John Doe")

class PacienteModelTest(TestCase):
    """
    Pruebas para el modelo Paciente.
    Verifica la creación y representación del objeto Paciente.
    """
    def setUp(self):
        self.paciente = Paciente.objects.create(nombre="Jane Doe", fecha_nacimiento=timezone.now())

    def test_paciente_creation(self):
        """Verifica que un paciente se puede crear correctamente."""
        self.assertTrue(isinstance(self.paciente, Paciente))
        self.assertEqual(str(self.paciente), "Jane Doe")

class CitaModelTest(TestCase):
    """
    Pruebas para el modelo Cita.
    Verifica la creación, asociación correcta de médico y paciente, y representación del objeto Cita.
    """
    def setUp(self):
        self.medico = Medico.objects.create(nombre="Dr. Jane Smith", especialidad="Oncología")
        self.paciente = Paciente.objects.create(nombre="John Smith", fecha_nacimiento=timezone.now())
        self.cita = Cita.objects.create(paciente=self.paciente, medico=self.medico, fecha=timezone.now(), motivo="Consulta regular")

    def test_cita_creation(self):
        """Verifica que una cita se puede crear correctamente."""
        self.assertTrue(isinstance(self.cita, Cita))
        self.assertEqual(str(self.cita), f"Cita de {self.paciente.nombre} con {self.medico.nombre}")

    def test_cita_medico_y_paciente(self):
        """Verifica que la cita está asociada al médico y al paciente correctos."""
        self.assertEqual(self.cita.paciente, self.paciente)
        self.assertEqual(self.cita.medico, self.medico)
