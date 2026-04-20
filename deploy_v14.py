import os

HTML_PATH = "index.html"
with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Restore BMC
bmc_start = html.find('<!-- Literal Copy 2: BMC -->')
bmc_end = html.find('<!-- Literal Copy 3: DPI Radar -->')

if bmc_start != -1 and bmc_end != -1:
    bmc_new = """<!-- Literal Copy 2: BMC -->
        <section id="bmc" class="section">
            <div class="container">
                <div class="title-wrapper">
                    <h2 class="section-title text-center text-black" data-i18n="bmc_title">Business Model Canvas</h2>
                    <div class="tooltip-container">i<span class="tooltip-text" data-i18n="tooltip_bmc">Estructura estratégica del modelo de negocio de UMO, diseñada a partir del análisis de capacidades internas y necesidades del mercado estadounidense.</span></div>
                </div>
                <div class="bmc-grid-complex">
                    <!-- Top Row -->
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_key_partners" class="text-black">Socios Clave (Key Partners)</h4>
                        <div data-i18n="bmc_kp_desc" class="bmc-inject"></div>
                    </div>
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_key_activities" class="text-black">Actividades Clave (Key Activities)</h4>
                        <div data-i18n="bmc_ka_desc" class="bmc-inject"></div>
                    </div>
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_key_resources" class="text-black">Recursos Clave (Key Resources)</h4>
                        <div data-i18n="bmc_kr_desc" class="bmc-inject"></div>
                    </div>
                    
                    <!-- Mid Row -->
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_customer_relation" class="text-black">Relaciones con Clientes (Customer Relationships)</h4>
                        <div data-i18n="bmc_cr_desc" class="bmc-inject"></div>
                    </div>
                    <div class="bmc-card card-shadow bmc-vp-solid">
                        <h4 data-i18n="bmc_value_prop" class="text-white">Propuesta de Valor (Value Proposition)</h4>
                        <div data-i18n="bmc_vp_desc" class="text-white bmc-inject text-justify"></div>
                    </div>
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_channels" class="text-black">Canales (Channels)</h4>
                        <div data-i18n="bmc_ch_desc" class="bmc-inject"></div>
                    </div>

                    <!-- Bottom Row -->
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_customer_segments" class="text-black">Segmentos de Clientes (Customer Segments)</h4>
                        <div data-i18n="bmc_cs_desc" class="bmc-inject"></div>
                    </div>
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_cost_structure" class="text-black">Estructura de Costos (Cost Structure)</h4>
                        <div data-i18n="bmc_cost_desc" class="bmc-inject"></div>
                    </div>
                    <div class="bmc-card card-shadow border-solid-black">
                        <h4 data-i18n="bmc_revenue" class="text-black">Fuentes de Ingresos (Revenue Streams)</h4>
                        <div data-i18n="bmc_rev_desc" class="bmc-inject"></div>
                    </div>
                </div>
            </div>
        </section>

        """
    html = html[:bmc_start] + bmc_new + html[bmc_end:]


# 2. Restore DOFA & Sostenibilidad
dofa_start = html.find('<!-- Literal Copy 5: DOFA -->')
dofa_end = html.find('<!-- Literal Copy 8: SMART Goal -->')

if dofa_start != -1 and dofa_end != -1:
    dofa_new = """<!-- Literal Copy 5: DOFA -->
        <section id="dofa" class="section bg-white">
            <div class="container">
                <div class="title-wrapper">
                    <h2 class="section-title text-center text-orange" data-i18n="dofa_title">Análisis DOFA de la Empresa UMO</h2>
                    <div class="tooltip-container" style="background-color:var(--orange);">i<span class="tooltip-text" data-i18n="tooltip_dofa">Matriz densa 2x2. Resultado de sesiones corporativas integradas en cruzamiento a reportes técnicos de alta envergadura automotriz foránea.</span></div>
                </div>
                <p class="intro-text text-gray text-center" data-i18n="intro_dofa">Diagnóstico transversal que categoriza los ejes orgánicos (virtudes y fricciones) expuestos perimetralmente sobre la exigencia técnica del entorno base en Estados Unidos.</p>
                <div class="dofa-grid-dense">
                    <!-- D -->
                    <div class="dofa-card card-shadow dofa-card-d text-white">
                        <div class="dofa-head text-white">
                            <h3 data-i18n="dofa_weak_title">Debilidades (D)</h3>
                        </div>
                        <div class="text-white text-justify dofa-inject" data-i18n="dofa_weak_desc"></div>
                    </div>
                    <!-- O -->
                    <div class="dofa-card card-shadow dofa-card-o text-black">
                        <div class="dofa-head text-black">
                            <h3 data-i18n="dofa_opp_title">Oportunidades (O)</h3>
                        </div>
                        <div class="text-black text-justify dofa-inject" data-i18n="dofa_opp_desc"></div>
                    </div>
                    <!-- F -->
                    <div class="dofa-card card-shadow dofa-card-f text-white">
                        <div class="dofa-head text-white">
                            <h3 data-i18n="dofa_str_title">Fortalezas (F)</h3>
                        </div>
                        <div class="text-white text-justify dofa-inject" data-i18n="dofa_str_desc"></div>
                    </div>
                    <!-- A -->
                    <div class="dofa-card card-shadow dofa-card-a text-white">
                        <div class="dofa-head text-white">
                            <h3 data-i18n="dofa_thr_title">Amenazas (A)</h3>
                        </div>
                        <div class="text-white text-justify dofa-inject" data-i18n="dofa_thr_desc"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Literal Copy 6: Sostenibilidad -->
        <section id="sustainability" class="section">
            <div class="container">
                <div class="title-wrapper">
                    <h2 class="section-title text-center text-black" data-i18n="sust_title">Sostenibilidad - UMO Dimensiones</h2>
                    <div class="tooltip-container">i<span class="tooltip-text" data-i18n="tooltip_sust">Ensamble de políticas globales ESG validando el accionar corporativo y el retorno económico limpio ante estándares multilaterales.</span></div>
                </div>
                <p class="intro-text text-gray text-center" data-i18n="intro_sust">La evaluación de factores es un bastión innegociable. Este análisis integra estructuralmente los conceptos abordados dentro del 'Podcast sobre sostenibilidad' de la plataforma, acoplándolos operativamente a la matriz de importación estadounidense.</p>
                <div class="sust-grid-dense mt-4">
                    <div class="sust-card card-shadow bg-white border-solid-black">
                        <div class="sust-circle bg-black"><svg viewBox="0 0 24 24" class="text-white">
                                <path fill="currentColor" d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z" />
                            </svg></div>
                        <h4 class="text-black text-center" data-i18n="sust_econ_title">Económico</h4>
                        <p class="text-justify" data-i18n="sust_econ_desc">En la dimensión económica, la empresa UMO tiene una trayectoria larga que muestra buena estabilidad... Esto demuestra que tienen una base económica sólida necesaria para competir internacionalmente y en temas de crecimiento B2B (CEPAL, 2021).</p>
                    </div>
                    <div class="sust-card card-shadow bg-black text-white">
                        <div class="sust-circle bg-white"><svg viewBox="0 0 24 24" class="text-black">
                                <path fill="currentColor" d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z" />
                            </svg></div>
                        <h4 class="text-white text-center" data-i18n="sust_social_title">Social</h4>
                        <p class="text-justify text-white" data-i18n="sust_social_desc">En la parte social, UMO es importante porque genera muchos empleos en el sector de autopartes, una de las grandes matrices de nuestra sociedad... Sin embargo, es necesario mejorar en temas de idiomas (como el inglés) para aprovechar mejor estas oportunidades en conjunto (OIT, 2022).</p>
                    </div>
                    <div class="sust-card card-shadow bg-white border-solid-black">
                        <div class="sust-circle bg-black"><svg viewBox="0 0 24 24" class="text-white">
                                <path fill="currentColor" d="M17 3H7c-1.1 0-1.99.9-1.99 2L5 21l7-3 7 3V5c0-1.1-.9-2-2-2z" />
                            </svg></div>
                        <h4 class="text-black text-center" data-i18n="sust_env_title">Ambiental</h4>
                        <p class="text-justify" data-i18n="sust_env_desc">Finalmente, en la dimensión ambiental, se identifican elementos importantes como el uso de materiales industriales que requieren control y gestión responsable. La existencia de un departamento de calidad indica que la empresa realiza mediciones... Además, su intención de ingresar a mercados como el de Estados Unidos implica el cumplimiento de normativas ambientales más exigentes, lo que promueve prácticas más sostenibles (ISO, 2015).</p>
                    </div>
                </div>
            </div>
        </section>

        """
    html = html[:dofa_start] + dofa_new + html[dofa_end:]
    print("SUCCESS: HTML written.")
else:
    print("FAILURE: HTML slices not found!")

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)
