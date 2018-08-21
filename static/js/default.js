/**
 * Default JS utilities
 */
var default_utilities = {
    // Disable link functionality for css class no-link
    no_link: function() {
        $("body").on("click", ".no-link", function() {
            return false;
        });
    },

    // Remove required attribute for some html elements
    remove_required: function() {
        $("input, select, textarea").removeAttr('required');
    },

    // Initialization
    init: function () {
        this.no_link();
        this.remove_required();
    }
};


/**
 * Document ready
 */
$(document).ready(function() {
    default_utilities.init();
});
