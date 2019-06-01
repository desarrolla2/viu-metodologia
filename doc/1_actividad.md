# Actividad 1

El proyecto de este semestre estará basado en el cultivo de orquídeas simplificado.
Para la primera entrega nos centraremos en lotes de orquídeas, invernaderos. Para su correcto
crecimiento y floración las orquídeas requieren ser trasladas de invernadero en una
determinada etapa de crecimiento. No entraremos en aspectos técnicos concretos, pero para
vuestro conocimiento deben pasar del frio y altitud de los andes al calor y altitud de la costa.

El menú permitirá 4 opciones:

1. Lotes de Orquídeas
1. Invernaderos
1. Simular
1. Info sistema
1. Salir

## Lotes de Orquídeas

Se pedirá al usuario los datos del lote:

- Un identificador alfanumérico del lote. Debe ser único, deben verificar que no existe ya en el sistema ese lote.
- Cantidad de plantas (Entero)
- Clima inicial (Andes o Costa)
- Días crecimiento Andes (Entero)
- Días crecimiento Costa (Entero)

Una vez introducido el lote correctamente, preguntará si queremos introducir otro Lote o salir al menú principal.

## Invernaderos

Se pedirá al usuario los datos del invernadero:

- Identificador alfanumérico único.
- Clima.
- Capacidad.

Un vez introducido el lote correctamente, preguntará si queremos introducir otro invernadero o salir al menú principal.

## Simular

Preguntará al usuario que quiere simular. Asignación de lotes o Paso de los días.

### Lotes

El sistema asigna automáticamente lotes a los invernaderos según sus características mientras tengan disponibilidad.
Debe ir mostrando por pantalla las asignaciones que va realizando.

### Días

Pide al usuario la cantidad de días a simular. Va avanzando día a día verificando si algún lote necesita ser trasladado. De ser necesario lo hace de forma automática, si no hay disponibilidad en los invernaderos que necesita da una alerta y destruye el lote.
Debe ir mostrando por pantalla todas las transacciones que realiza.

## Info Sistema

Muestra la información del estado del sistema. Agrupada por Lotes sin asignar y Invernaderos donde indicara que lotes tienen y en qué estado.

## Salir

Sale del programa.

## Ampliación (puntos adicionales):

Algunos de vosotros tenéis un conocimiento mayor del Python y de programación. Podéis complicar un poco el proyecto considerando para los lotes una temperatura ideal y en los invernaderos indicar un rango de temperaturas. Para la asignación se deberá comprobar que la temperatura ideal del lote este entre el rango de trabajo del invernadero.
También podéis implementar que la asignación se inicie según la preferencia que indique el usuario de lotes con más a menos plantas o a la inversa.