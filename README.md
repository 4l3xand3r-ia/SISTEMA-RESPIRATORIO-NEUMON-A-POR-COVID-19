[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=4l3xand3r-ia/SISTEMA-RESPIRATORIO-NEUMON-A-POR-COVID-19)

# Sistema respiratorio: Neumonía por COVID-19

## Estudiantes
Venegas Ornelas Lizeth Guadalupe, Torres Avila Alexander, Patraca Toledo Abishnaed
Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: l21212671@tectijuana.edu.mx; l21212848@tectijuana.edu.mx; l21212172@tectijuana.edu.mx

## Asignaturas o departmento donde se puede usar la Actividad
Modelado de Sistemas Fisiológicos de Ingeniería Biomédica

## Información general
El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivo general
Diseñar un gemelo digital de un sistema fisiológico que permita identificar las diferencias entre un paciente afectado por una enfermedad (caso) y un individuo saludable (control) para desarrollar un protocolo de tratamiento mediante un sistema de control en lazo cerrado.

## Descripción detallada del sistema
El sistema simula la dinámica de las presiones y flujos de aire en las vías respiratorias y alvéolos para analizar la mecánica respiratoria en pacientes con neumonía por COVID-19, comparando un individuo sano con un paciente crítico. Utiliza un modelo basado en un circuito RLC de dos mallas que representa:
Primera malla: Incluye una fuente de voltaje (presión de inspiración), un resistor R1R1R1 (resistencia de vías principales), un inductor L1 (inercia del flujo) y un capacitor C1 (elasticidad pulmonar). La corriente I1 se divide en dos: una parte hacia C1 y otra hacia la segunda malla.
Segunda malla: Contiene un resistor R2 y un inductor L2 en serie (resistencia e inercia a nivel alveolar), y capacitores C2 (elasticidad alveolar) y C3 (distensibilidad de vías centrales) en paralelo.
El modelo permite evaluar cómo inflamación, secreciones y daño alveolar afectan el flujo y la presión respiratoria, ofreciendo una representación precisa de las dinámicas pulmonares en condiciones críticas.

## Referencias principales
[1] National Heart, Lung and Blood Institute. “¿Qué es la neumonía?” NHLBI, NIH. [En línea]. Disponible: https://www.nhlbi.nih.gov/es/salud/neumonia#:~:text=La%20neumonía%20es%20una%20infección,hongos%20que%20pueden%20provocar%20neumonía.

[2] D. A. Menchén, J. B. Vázquez, J. M. B. Allende y G. H. García, “Neumonía vírica. Neumonía en la COVID-19”, Med. - Programa Form. Medica Contin. Acreditado, vol. 13, n.º 55, pp. 3224–3234, mayo de 2022. Accedido el 11 de diciembre de 2024. [En línea]. Disponible: https://doi.org/10.1016/j.med.2022.05.003
