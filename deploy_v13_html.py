import os

HTML_PATH = "index.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

bmc_start = html.find('<!-- Literal Copy 2: BMC -->')
bmc_end = html.find('<!-- Literal Copy 3: DPI Radar -->')

if bmc_start != -1 and bmc_end != -1:
    bmc_new = """        <!-- Literal Copy 2: BMC -->
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
                        <h4 data-i18n="bmc_customer_relation" class="text-black">Relación con Clientes (Customer Relationships)</h4>
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

dofa_start = html.find('<div class="dofa-grid-dense">')
dofa_end = html.find('<!-- Literal Copy 6: Sostenibilidad -->')

if dofa_start != -1 and dofa_end != -1:
    dofa_new = """<div class="dofa-grid-dense">
                    <!-- D -->
                    <div class="dofa-card card-shadow dofa-card-d text-white">
                        <div class="dofa-head text-white">
                            <h3 data-i18n="dofa_weak_title" class="text-white">Debilidades (D)</h3>
                        </div>
                        <div class="text-white text-justify dofa-inject" data-i18n="dofa_weak_desc"></div>
                    </div>
                    <!-- O -->
                    <div class="dofa-card card-shadow dofa-card-o text-black">
                        <div class="dofa-head text-black">
                            <h3 data-i18n="dofa_opp_title" class="text-black">Oportunidades (O)</h3>
                        </div>
                        <div class="text-black text-justify dofa-inject" data-i18n="dofa_opp_desc"></div>
                    </div>
                    <!-- F -->
                    <div class="dofa-card card-shadow dofa-card-f text-white">
                        <div class="dofa-head text-white">
                            <h3 data-i18n="dofa_str_title" class="text-white">Fortalezas (F)</h3>
                        </div>
                        <div class="text-white text-justify dofa-inject" data-i18n="dofa_str_desc"></div>
                    </div>
                    <!-- A -->
                    <div class="dofa-card card-shadow dofa-card-a text-white">
                        <div class="dofa-head text-white">
                            <h3 data-i18n="dofa_thr_title" class="text-white">Amenazas (A)</h3>
                        </div>
                        <div class="text-white text-justify dofa-inject" data-i18n="dofa_thr_desc"></div>
                    </div>
                </div>
            </div>
        </section>

        """
    html = html[:dofa_start] + dofa_new + html[dofa_end:]

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML Restructured")
