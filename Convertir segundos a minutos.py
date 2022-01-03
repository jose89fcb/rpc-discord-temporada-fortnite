def segundos_a_dhms(tiempo):
    segundos_a_minutos   = 60
    segundos_a_horas     = 60 * segundos_a_minutos
    segundos_a_dias      = 24 * segundos_a_horas

    dias    =   tiempo // segundos_a_dias
    tiempo    %=  segundos_a_dias

    horas   =   tiempo // segundos_a_horas
    tiempo   %=  segundos_a_horas

    minutos =   tiempo // segundos_a_minutos
    tiempo    %=  segundos_a_minutos

    segundos = tiempo

    print("%d dias, %d horas, %d minutos, %d segundos" % (dias, horas, minutos, segundos))


time = int(input("Escribe el número en segundos: "))
segundos_a_dhms(time)