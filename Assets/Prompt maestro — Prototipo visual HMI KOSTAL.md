# Prompt maestro — Prototipo visual HMI KOSTAL

Quiero desarrollar un **prototipo visual UX/UI de una interfaz HMI industrial para KOSTAL**.

IMPORTANTE: en esta etapa debe ser principalmente un **cascarón visual / mockup de alta fidelidad**. No desarrollar lógica industrial real, conexión con PLC, base de datos, APIs, autenticación real ni procesamiento de datos.

El objetivo es presentar cómo debería verse y organizarse la interfaz antes de comenzar el desarrollo funcional.

## 1. Referencias visuales

Utiliza como referencia los mockups manuales proporcionados y el logotipo oficial de KOSTAL.

Los mockups sirven para entender:

- distribución general;
- jerarquía de información;
- ubicación aproximada de elementos;
- flujo entre ventanas;
- componentes requeridos.

NO copies literalmente el estilo dibujado a mano.

Transforma los mockups en una interfaz industrial moderna, profesional, limpia y consistente.

El resultado debe parecer una HMI real diseñada para instalarse en una máquina industrial de KOSTAL.

---

# 2. Identidad visual

Basar la interfaz principalmente en los colores del logotipo KOSTAL proporcionado.

Paleta principal aproximada:

- Azul marino KOSTAL como color principal.
- Blanco.
- Gris muy claro para fondos.
- Gris medio para divisores, bordes y elementos secundarios.
- Texto principal en azul marino oscuro / gris muy oscuro.

Utilizar colores semánticos solamente cuando sea necesario:

- Verde: estado OK / sistema activo.
- Rojo: NOK / alarma / paro.
- Amarillo o ámbar: advertencia.

Estos colores deben ser acentos y no dominar el diseño.

Evitar:

- degradados excesivos;
- efectos futuristas;
- neón;
- sombras exageradas;
- interfaces demasiado oscuras;
- estilo de aplicación móvil;
- exceso de botones redondeados.

Debe transmitir:

**Ingeniería + precisión + manufactura + limpieza + confiabilidad.**

Inspiración estética:

- Siemens Industrial HMI;
- Beckhoff;
- Bosch Rexroth;
- Festo;
- interfaces MES modernas;
- dashboards industriales premium.

Pero manteniendo claramente la identidad visual KOSTAL.

---

# 3. Principios generales UX/UI

Diseñar pensando en una pantalla táctil industrial.

Características:

- botones grandes;
- excelente legibilidad;
- jerarquía clara;
- suficiente separación entre controles;
- textos simples;
- pocos elementos decorativos;
- lectura rápida a distancia;
- elementos táctiles fáciles de seleccionar;
- consistencia entre todas las pantallas.

Usar una estructura visual basada en:

**Header + área principal + indicadores + navegación según permisos.**

Crear componentes reutilizables para:

- encabezados;
- botones;
- cards;
- indicadores;
- tablas;
- modales;
- campos;
- badges;
- contadores;
- navegación.

---

# 4. Arquitectura general de pantallas

Crear inicialmente las siguientes pantallas:

1. Login
2. Pantalla principal del operador
3. Panel administrativo
   - Ventana 1: Programas / modelos / recetas
   - Ventana 2: Estadísticas
   - Ventana 3: Usuarios
4. Pantalla flotante PF1 para configuración de programa/modelo.

---

# 5. Pantalla de LOGIN

Crear una pantalla de inicio de sesión extremadamente limpia.

Mostrar:

- logotipo KOSTAL;
- nombre provisional del sistema;
- campo Usuario;
- campo Contraseña;
- botón “Iniciar sesión”.

Existen solamente dos niveles de credenciales:

### OPERADOR
Usuario de producción.

### ADMIN
Administrador del sistema.

No implementar autenticación real.

Utilizar datos ficticios solamente para representar visualmente ambos niveles.

En el prototipo puede existir una forma sencilla de visualizar ambos escenarios.

---

# 6. Rol OPERADOR

El operador debe tener una interfaz extremadamente sencilla.

No debe tener acceso a:

- creación de usuarios;
- configuración avanzada;
- edición de programas;
- estadísticas administrativas;
- parámetros de máquina.

Después de iniciar sesión como operador debe mostrarse directamente la:

# PANTALLA PRINCIPAL

Basarse visualmente en el primer mockup proporcionado.

---

# 7. Pantalla principal del operador

Esta será la pantalla que permanece visible durante la producción.

Debe tener una estructura industrial muy clara.

## HEADER

En la parte superior mostrar:

- logo KOSTAL;
- nombre o código de la estación;
- usuario activo;
- rol: OPERADOR;
- fecha;
- hora;
- indicador de estado de máquina.

Ejemplo de estado:

● SISTEMA LISTO

También mostrar un botón discreto para cerrar sesión.

---

# 8. Temporizador de jornada

Cuando el operador inicia sesión, conceptualmente comenzará el registro de su jornada.

Para este prototipo solamente representarlo visualmente.

Mostrar algo como:

**Sesión activa**

Operador:
Juan Pérez

Inicio:
07:31:24

Tiempo de sesión:
02:14:32

El temporizador puede ser visual / simulado.

---

# 9. Información que eventualmente registrará el sistema

Aunque todavía no se implementará la lógica, diseñar la interfaz considerando que en el futuro se registrarán:

- usuario;
- rol;
- fecha;
- hora de inicio de sesión;
- hora de cierre de sesión;
- duración de sesión;
- hora de primera secuencia;
- tiempo desde login hasta primera secuencia;
- producto;
- modelo;
- programa;
- matriz;
- cantidad total producida;
- piezas OK;
- piezas NOK;
- porcentaje OK;
- porcentaje NOK.

La definición técnica para determinar si una pieza es OK o NOK está todavía pendiente.

Por ahora usar valores simulados.

---

# 10. Área principal de piezas

La zona central de la pantalla debe ser el elemento visual dominante.

Representar una matriz de piezas similar al primer mockup.

Ejemplo:

3 columnas × 5 filas.

Cada posición representa físicamente una pieza del fixture o matriz.

IMPORTANTE:

Las figuras de los mockups son solamente una representación conceptual de las piezas.

Crear placeholders gráficos limpios para las piezas.

Cada pieza debe estar dentro de una celda clara.

Estados visuales futuros:

- pendiente;
- activa;
- procesada OK;
- procesada NOK.

Ejemplo:

Pendiente:
gris claro.

Activa:
contorno azul KOSTAL.

OK:
pequeño indicador verde.

NOK:
pequeño indicador rojo.

NO hacer que toda la pieza cambie a colores intensos.

Mantener una estética sobria.

---

# 11. Información del producto

Cerca de la matriz mostrar una card con:

**Producto actual**

Modelo:
XXXXXX

Programa:
P01

Matriz:
3 × 5

Piezas programadas:
15

Piezas realizadas:
08 / 15

Estos datos son ficticios.

---

# 12. Contadores de producción

Crear indicadores grandes y legibles.

Ejemplo:

TOTAL
128

OK
124

NOK
4

También puede mostrarse:

CALIDAD
96.9%

Los indicadores deben verse industriales y no como widgets de una aplicación de ventas.

---

# 13. Botón principal OPERADOR

De acuerdo con los requerimientos, el operador solamente tendrá un control principal de operación.

Crear un botón grande:

**ON**

Debe ser visualmente muy claro.

Cuando está apagado:

○ OFF / LISTO

Cuando visualmente se representa activo:

● ON / CICLO ACTIVO

Para el mockup puede existir únicamente el diseño de ambos estados.

No implementar lógica real.

---

# 14. Indicador de primera secuencia

Diseñar un pequeño indicador que permita visualizar conceptualmente:

Inicio de sesión:
07:31:24

Primera secuencia:
07:36:51

Tiempo hasta primera secuencia:
05:27

Esto será importante posteriormente para análisis de productividad.

Puede aparecer en una sección discreta de información de jornada.

---

# 15. Panel administrativo

Cuando se utiliza un usuario ADMIN debe aparecer una interfaz diferente.

El administrador tendrá acceso a tres ventanas principales.

Crear navegación lateral izquierda.

Logo KOSTAL en la parte superior.

Después:

### Ventana 1
Programas

### Ventana 2
Estadísticas

### Ventana 3
Usuarios

En la parte inferior de la navegación:

Usuario:
Admin

Rol:
ADMIN

Cerrar sesión

Utilizar iconos simples acompañados de texto.

No utilizar navegación basada solamente en iconos.

---

# 16. VENTANA 1 — PROGRAMAS

Basarse en el segundo mockup.

Esta debe ser una pantalla de administración de modelos / programas / recetas de producción.

Título:

# Programas de producción

Subtítulo:

Configuración de productos, matrices y coordenadas.

Crear una tabla limpia.

Columnas sugeridas:

- Nombre
- Modelo
- Programa
- Matriz
- Distancia X
- Distancia Y
- Última modificación
- Estado
- Acciones

Ejemplo:

| Nombre | Modelo | Programa | Matriz | X | Y | Estado |
| Botón A | KSL-001 | P01 | 3×5 | 42 mm | 36 mm | Activo |

En “Acciones” colocar:

- Editar
- Configurar

Utilizar iconos acompañados de tooltip.

---

# 17. Acción JOG / configuración

De acuerdo con el segundo mockup existe una acción que debe permitir abrir una ventana flotante.

Representarla mediante un botón:

**Configurar posición**

o

**JOG / Configuración**

Al seleccionarlo visualmente debe abrirse:

# PF1

La Pantalla Flotante 1.

---

# 18. PF1 — Pantalla flotante de configuración

Basarse directamente en el tercer mockup pero rediseñarlo completamente con un UX/UI profesional.

PF1 debe presentarse como un modal grande o panel flotante.

Título:

# Configuración de programa

Subtítulo:

Modelo / matriz / posicionamiento

---

## Información general

Campos:

Nombre

[___________]

Modelo

[___________]

Programa

[___________]

Matriz

[ 3 ] × [ 5 ]

---

# 19. Configuración de distancia X

Crear una sección:

### Distancia entre centros X

Campo:

[ 42.00 ] mm

Debajo colocar controles visuales de movimiento tipo JOG:

            ↑

       ←    ●    →

            ↓

Los botones deben ser cuadrados, robustos y táctiles.

Agregar adicionalmente:

- X+
- X-
- Y+
- Y-

si mejora la claridad del diseño.

---

# 20. Configuración eje / referencia

En la zona derecha mostrar botones:

SET 0

SUBIR

BAJAR

Los botones deben tener iconografía industrial sencilla.

SET 0 debe diferenciarse visualmente de movimiento normal.

---

# 21. Distancia Y

Crear otra sección:

### Distancia entre centros Y

Campo:

[ 36.00 ] mm

Utilizar la misma consistencia visual que en X.

---

# 22. Guardar

En la zona inferior derecha colocar un botón principal:

**GUARDAR CONFIGURACIÓN**

Color principal azul KOSTAL.

Agregar botón secundario:

Cancelar

---

# 23. Información inferior PF1

El mockup original incluye una zona de “Estadísticas e Información”.

Conservar el concepto pero hacerlo limpio.

Crear una sección inferior con información contextual.

Ejemplo:

Programa:
P01

Última modificación:
25/08/2026 10:42

Modificado por:
Admin

Matriz:
3 × 5

Distancia X:
42.00 mm

Distancia Y:
36.00 mm

Estado:
Activo

Esto es solamente visual.

---

# 24. VENTANA 2 — ESTADÍSTICAS

Crear una pantalla profesional de datos de producción.

Título:

# Estadísticas de producción

Debe existir una zona superior de filtros.

Filtros visuales:

Fecha desde

Fecha hasta

Usuario

Modelo

Programa

Turno

Estado

Botón:

FILTRAR

No implementar lógica real.

---

# 25. KPIs de estadísticas

Antes de la tabla mostrar pequeñas cards con:

TOTAL PIEZAS

PIEZAS OK

PIEZAS NOK

% CALIDAD

TIEMPO PROMEDIO LOGIN → PRIMERA SECUENCIA

TIEMPO PROMEDIO DE SESIÓN

Utilizar valores ficticios.

Ejemplo:

Total:
1,428

OK:
1,392

NOK:
36

Calidad:
97.5%

Login → Primera secuencia:
04:18

---

# 26. Tabla histórica

Crear tabla principal con:

- Fecha
- Usuario
- Inicio sesión
- Primera secuencia
- Tiempo hasta primera secuencia
- Modelo
- Programa
- Total
- OK
- NOK
- % OK
- Fin de sesión
- Duración jornada

Ejemplo de registro:

25/08/2026  
Juan Pérez  
07:31:24  
07:36:51  
00:05:27  
KSL-001  
P01  
328  
321  
7  
97.8%  
16:02:18  
08:30:54

Crear aproximadamente 8 registros ficticios para que la tabla se vea real.

---

# 27. VENTANA 3 — USUARIOS

Aquí existe libertad creativa UX/UI.

Debe ser una pantalla extremadamente clara y profesional.

Título:

# Gestión de usuarios

Subtítulo:

Administración de operadores y administradores.

Solamente usuarios ADMIN podrán visualizar esta pantalla.

Solamente ADMIN puede agregar, modificar, activar o desactivar usuarios.

---

# 28. Dashboard de usuarios

Crear tres pequeños indicadores:

Usuarios activos

Operadores

Administradores

Ejemplo:

18 activos

15 operadores

3 administradores

---

# 29. Tabla de usuarios

Columnas:

- ID
- Nombre
- Usuario
- Rol
- Estado
- Último acceso
- Última jornada
- Acciones

Roles:

OPERADOR

ADMIN

Estados:

Activo

Inactivo

Usar badges discretos.

---

# 30. Crear usuario

Agregar botón superior derecho:

**+ NUEVO USUARIO**

Debe abrir visualmente un modal.

Campos:

Nombre completo

Número de empleado

Nombre de usuario

Contraseña

Confirmar contraseña

Rol:

Operador

Administrador

Estado:

Activo

Botones:

CANCELAR

CREAR USUARIO

No implementar almacenamiento real.

---

# 31. Detalle de operador

Al seleccionar un operador permitir visualizar conceptualmente un panel lateral o modal.

Mostrar:

Nombre

Número de empleado

Usuario

Rol

Estado

Último inicio de sesión

Total jornadas registradas

Tiempo promedio de inicio → primera secuencia

Piezas producidas

Piezas OK

Piezas NOK

Última jornada

Esto prepara visualmente la interfaz para futuras funcionalidades de productividad por operador.

---

# 32. Seguridad visual por rol

La interfaz debe comunicar claramente qué puede realizar cada rol.

## OPERADOR

Puede:

- iniciar sesión;
- visualizar programa activo;
- visualizar piezas;
- visualizar avance;
- visualizar contadores;
- utilizar el botón ON;
- cerrar sesión.

NO puede:

- crear usuarios;
- modificar usuarios;
- cambiar parámetros;
- modificar coordenadas;
- editar programas;
- acceder a configuración administrativa.

## ADMIN

Puede visualizar visualmente:

- programas;
- estadísticas;
- usuarios;
- configuración;
- PF1.

No desarrollar todavía permisos reales.

---

# 33. Estados de máquina

Crear un componente reutilizable de estado.

Ejemplos:

SISTEMA LISTO

CICLO ACTIVO

ESPERANDO OPERADOR

SECUENCIA TERMINADA

ADVERTENCIA

NOK DETECTADO

El estado debe aparecer de forma prominente pero limpia.

---

# 34. Diseño de tablas

Todas las tablas deben utilizar:

- encabezado fijo visual;
- filas perfectamente alineadas;
- separación suave;
- buen contraste;
- hover muy discreto;
- tipografía industrial limpia;
- badges para estados;
- iconos mínimos.

Evitar líneas negras gruesas.

---

# 35. Tipografía

Utilizar una tipografía sans-serif moderna de excelente legibilidad.

Preferiblemente:

Inter

o equivalente.

Jerarquía aproximada:

Título:
28–32 px

Subtítulo:
18–20 px

Texto:
14–16 px

Datos importantes:
24–36 px

Botones:
16–18 px

La interfaz debe poder leerse cómodamente en una pantalla industrial.

---

# 36. Dimensiones

Diseñar inicialmente tomando como referencia:

1920 × 1080 px.

Mantener layout responsive razonable para otras resoluciones industriales.

No diseñar pensando primero en smartphone.

Desktop / HMI industrial es la prioridad.

---

# 37. Iconografía

Usar iconografía simple y consistente.

Ejemplos:

- usuario;
- estadísticas;
- configuración;
- programa;
- editar;
- play;
- stop;
- subir;
- bajar;
- izquierda;
- derecha;
- guardar;
- logout.

No utilizar emojis.

---

# 38. Nivel visual esperado

Quiero que visualmente parezca un producto suficientemente maduro como para presentarlo frente a:

- ingeniería de manufactura;
- producción;
- calidad;
- mantenimiento;
- gerencia de planta.

No debe parecer:

- proyecto escolar;
- dashboard genérico;
- página web;
- template administrativo;
- ERP convencional.

Debe parecer una verdadera interfaz de máquina industrial desarrollada específicamente para KOSTAL.

---

# 39. Microinteracciones

Aunque la aplicación no tendrá lógica funcional todavía, crear estados visuales para:

- hover;
- pressed;
- selected;
- disabled;
- active;
- warning;
- error;
- success.

Las transiciones deben ser rápidas y discretas.

---

# 40. Alcance técnico de esta primera etapa

NO implementar:

- PLC;
- OPC UA;
- Modbus;
- IO-Link;
- comunicación industrial;
- bases de datos;
- backend;
- APIs;
- control real de ejes;
- autenticación real;
- registro real de jornadas;
- cálculos OEE;
- algoritmos OK/NOK;
- persistencia;
- lógica productiva.

Utilizar exclusivamente información ficticia.

Si se requiere navegación para demostrar el diseño, puede ser una navegación local simulada entre pantallas, sin backend ni lógica real.

---

# 41. Datos ficticios

Llenar las interfaces con suficientes datos ficticios para que se pueda evaluar correctamente el diseño.

No utilizar Lorem Ipsum.

Utilizar información industrial coherente.

Ejemplos:

Usuarios:

Juan Pérez  
Operador

María López  
Operador

Carlos Hernández  
Admin

Modelos:

KSL-001

KSL-002

KSL-003

Programas:

P01

P02

P03

---

# 42. Componentes prioritarios

Antes de terminar, verificar que existan visualmente:

- login;
- identidad KOSTAL;
- pantalla operador;
- usuario activo;
- temporizador de sesión;
- matriz visual de piezas;
- progreso;
- total piezas;
- OK;
- NOK;
- botón ON;
- menú administrativo;
- Programas;
- Estadísticas;
- Usuarios;
- tabla de programas;
- tabla de producción;
- tabla de usuarios;
- PF1;
- controles JOG;
- SET 0;
- SUBIR;
- BAJAR;
- GUARDAR.

---

# 43. Criterio final

Priorizar en este orden:

1. Claridad para el operador.
2. Seguridad visual.
3. Facilidad de lectura.
4. Apariencia industrial profesional.
5. Consistencia.
6. Identidad KOSTAL.
7. Simplicidad.
8. Estética.

Cuando exista duda entre agregar una función visual adicional o mantener la pantalla sencilla:

**mantenerla sencilla.**

Genera primero todo el frontend visual de esta primera versión y mantén el código organizado para que posteriormente podamos ir refinando cada pantalla individualmente.