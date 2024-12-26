frappe.pages['union-dashboard'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'لوحة التحكم',
        single_column: true
    });

    // Add dashboard content
    page.main.html(`
        <div class="union-dashboard">
            <div class="row">
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">إحصائيات العضوية</h5>
                            <div id="membership-stats"></div>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">التقارير المالية</h5>
                            <div id="financial-summary"></div>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">الدورات التدريبية</h5>
                            <div id="training-summary"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `);

    // Load dashboard data
    load_dashboard_data(page);
}

function load_dashboard_data(page) {
    frappe.call({
        method: 'education_union.education_union.page.union_dashboard.union_dashboard.get_dashboard_data',
        callback: function(r) {
            if (r.message) {
                update_dashboard(r.message);
            }
        }
    });
}

function update_dashboard(data) {
    if (data) {
        $('#membership-stats').html(`
            <p>إجمالي الأعضاء: ${data.total_members}</p>
            <p>البطاقات النشطة: ${data.active_cards}</p>
            <p>البطاقات المعلقة: ${data.pending_cards}</p>
        `);
    }
} 