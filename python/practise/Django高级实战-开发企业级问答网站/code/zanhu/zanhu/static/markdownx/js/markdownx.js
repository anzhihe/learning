(function e(t, n, r) {
    function s(o, u) {
        if (!n[o]) {
            if (!t[o]) {
                var a = typeof require == "function" && require;
                if (!u && a) return a(o, !0);
                if (i) return i(o, !0);
                var f = new Error("Cannot find module '" + o + "'");
                throw f.code = "MODULE_NOT_FOUND", f
            }
            var l = n[o] = {exports: {}};
            t[o][0].call(l.exports, function (e) {
                var n = t[o][1][e];
                return s(n ? n : e)
            }, l, l.exports, e, t, n, r)
        }
        return n[o].exports
    }

    var i = typeof require == "function" && require;
    for (var o = 0; o < r.length; o++) s(r[o]);
    return s
})({
    1: [function (require, module, exports) {
        /**
         * **Markdownx**
         *
         * Frontend (JavaScript) management of Django-MarkdownX package.
         *
         * Written in JavaScript ECMA 2016, trans-compiled to ECMA 5 (2011).
         *
         * Requirements:
         * - Modern browser with support for HTML5 and ECMA 2011+ (IE 10+). Older browsers would work but some
         *   features may be missing
         * - TypeScript 2 +
         *
         * JavaScript ECMA 5 files formatted as `.js` are trans-compiled files. Please do not edit such files as all
         * changes will be lost. Please modify `.ts` stored in `django-markdownx/markdownx/.static/markdownx/js` directory.
         * See **Contributions** in the documentations for additional instructions.
         *
         * @Copyright 2017 - Adi, Pouria Hadjibagheri.
         */
// Import, definitions and constant ------------------------------------------------------------------------------------
        "use strict";
        Object.defineProperty(exports, "__esModule", {value: true});
        var utils_1 = require("./utils");
        var UPLOAD_URL_ATTRIBUTE = "data-markdownx-upload-urls-path", PROCESSING_URL_ATTRIBUTE = "data-markdownx-urls-path",
            RESIZABILITY_ATTRIBUTE = "data-markdownx-editor-resizable", LATENCY_ATTRIBUTE = "data-markdownx-latency", LATENCY_MINIMUM = 500, // microseconds.
            XHR_RESPONSE_ERROR = "Invalid response", UPLOAD_START_OPACITY = "0.3", NORMAL_OPACITY = "1";
// ---------------------------------------------------------------------------------------------------------------------
        /**
         *
         */
        var EventHandlers = {
            /**
             * Routine tasks for event handlers (e.g. default preventions).
             *
             * @param {Event} event
             * @returns {Event}
             */
            inhibitDefault: function (event) {
                event.preventDefault();
                event.stopPropagation();
                return event;
            },
            /**
             *
             * @param {DragEvent} event
             * returns {Event}
             */
            onDragEnter: function (event) {
                event.dataTransfer.dropEffect = 'copy';
                return EventHandlers.inhibitDefault(event);
            }
        };
        /**
         *
         */
        var keyboardEvents = {
            /**
             * Custom hotkeys.
             */
            keys: {
                TAB: "Tab",
                DUPLICATE: "d",
                UNINDENT: "[",
                INDENT: "]"
            },
            /**
             * Hotkey response functions.
             */
            handlers: {
                /**
                 * Smart application of tab indentations under various conditions.
                 *
                 * @param {JSON} properties
                 * @returns {string}
                 */
                applyTab: function (properties) {
                    // Do not replace with variables; this
                    // feature is optimised for swift response.
                    return properties.value
                            .substring(0, properties.start) +
                        (properties.value
                                .substring(properties.start, properties.end) // Selected text
                                .match(/\n/gm) === null ?
                                "\t" + properties.value.substring(properties.start) :
                                properties.value // Otherwise:
                                    .substring(properties.start, properties.end)
                                    .replace(/^/gm, '\t') +
                                properties.value.substring(properties.end) // Succeeding text.
                        );
                },
                /**
                 * Smart removal of tab indentations.
                 *
                 * @param {JSON} properties
                 * @returns {string}
                 */
                removeTab: function (properties) {
                    var substitution = null, lineTotal = (properties.value
                            .substring(properties.start, properties.end).match(/\n/g) || [] // Number of lines (\n) or empty array (zero).
                    ).length; // Length of the array is equal to the number of lines.
                    if (properties.start === properties.end) {
                        // Replacing `\t` at a specific location
                        // (+/- 1 chars) where there is no selection.
                        properties.start =
                            properties.start > 0 &&
                            properties.value[properties.start - 1] // -1 is to account any tabs just before the cursor.
                                .match(/\t/) !== null ?
                                properties.start - 1 : properties.start;
                        substitution = properties.value
                            .substring(properties.start)
                            .replace("\t", ''); // Remove only a single `\t`.
                    } else if (!lineTotal) {
                        // Replacing `\t` within a single line selection.
                        substitution =
                            properties.value
                                .substring(properties.start)
                                .replace("\t", '');
                    } else {
                        // Replacing `\t` in the beginning of each line
                        // in a multi-line selection.
                        substitution =
                            properties.value.substring(properties.start, properties.end).replace(/^\t/gm, '') +
                            properties.value.substring(properties.end); // After the selection
                    }
                    return properties.value
                            .substring(0, properties.start) +
                        substitution;
                },
                /**
                 * Handles multi line indentations.
                 *
                 * @param {JSON} properties
                 * @returns {string}
                 * @private
                 */
                _multiLineIndentation: function (properties) {
                    // Last line in the selection; regardless of
                    // where of not the entire line is selected.
                    var endLine = new RegExp("(?:\n|.){0," + properties.end + "}(^.*$)", "m")
                        .exec(properties.value)[1];
                    // Do not replace with variables; this
                    // feature is optimised for swift response.
                    return properties.value.substring(
                        // First line of the selection, regardless of
                        // whether or not the entire line is selected.
                        properties.value.indexOf(new RegExp("(?:\n|.){0," + properties.start + "}(^.*$)", "m")
                            .exec(properties.value)[1] // Start line.
                        ), (
                            // If there is a last line in a multi line selected
                            // value where the last line is not empty or `\n`:
                            properties.value.indexOf(endLine) ?
                                // Location where the last line finishes with
                                // respect to the entire value.
                                properties.value.indexOf(endLine) + endLine.length :
                                // Otherwise, where the selection ends.
                                properties.end));
                },
                /**
                 * Smart application of indentation at the beginning of the line.
                 *
                 * @param {JSON} properties
                 * @returns {string}
                 */
                applyIndentation: function (properties) {
                    // Single line?
                    if (properties.start === properties.end) {
                        // Current line, from the beginning to the end, regardless of any selections.
                        var line = new RegExp("(?:\n|.){0," + properties.start + "}(^.+$)", "m")
                            .exec(properties.value)[1];
                        return properties.value.replace(line, "\t" + line);
                    }
                    // Multi line
                    var content = this._multiLineIndentation({
                        start: properties.start,
                        end: properties.end,
                        value: properties.value
                    });
                    return properties.value
                        .replace(content, // Existing contents.
                            content.replace(/(^.+$)\n*/gmi, "\t$&") // Indented contents.
                        );
                },
                /**
                 * Smart removal of indentation from the beginning of the line.
                 *
                 * @param {JSON} properties
                 * @returns {string}
                 */
                removeIndentation: function (properties) {
                    // Single Line
                    if (properties.start === properties.end) {
                        // Entire line where the line immediately begins
                        // with a one or more `\t`, regardless of any
                        // selections.
                        var line = new RegExp("(?:\n|.){0," + properties.start + "}(^\t.+$)", "m")
                            .exec(properties.value)[1];
                        return properties.value
                            .replace(line, // Existing content.
                                line.substring(1) // First character (necessarily a `\t`) removed.
                            );
                    }
                    // Multi line
                    var content = this._multiLineIndentation({
                        start: properties.start,
                        end: properties.end,
                        value: properties.value
                    });
                    return properties.value
                        .replace(content, // Existing content.
                            content.replace(/^\t(.+)\n*$/gmi, "$1") // A single `\t` removed from the beginning.
                        );
                },
                /**
                 * Duplication of the current or selected lines.
                 *
                 * @param {JSON} properties
                 * @returns {string}
                 */
                applyDuplication: function (properties) {
                    // With selection.
                    // Do not replace with variables. This
                    // feature is optimised for swift response.
                    if (properties.start !== properties.end)
                        return (properties.value.substring(// Text preceding the selected area.
                                0, properties.start) +
                            properties.value.substring(// Selected area
                                properties.start, properties.end) +
                            (~properties.value // First character before the cursor is linebreak?
                                    .charAt(properties.start - 1)
                                    .indexOf('\n') ||
                                ~properties.value // Character on the cursor is linebreak?
                                    .charAt(properties.start)
                                    .indexOf('\n') ? '\n' : '' // If either, add linebreak, otherwise add nothing.
                            ) +
                            properties.value.substring(// Selected area (again for duplication).
                                properties.start, properties.end) +
                            properties.value.substring(properties.end) // Text succeeding the selected area.
                        );
                    // Without selection.
                    var pattern = new RegExp("(?:.|\n){0,160}(^.*$)", 'm'), line = '';
                    // Add anything found to the `line`. Note that
                    // `replace` is used a simple hack; it functions
                    // in a similar way to `regex.search` in Python.
                    properties.value
                        .replace(pattern, function (match, p1) {
                            return line += p1;
                        });
                    return properties.value
                        .replace(line, // Existing line.
                            line + "\n" + line // Doubled ... magic!
                        );
                },
            },
            /**
             * Mapping of hotkeys from keyboard events to their corresponding functions.
             *
             * @param {KeyboardEvent} event
             * @returns {Function | Boolean}
             */
            hub: function (event) {
                switch (event.key) {
                    case this.keys.TAB:
                        // Shift pressed: un-indent, otherwise indent.
                        return event.shiftKey ? this.handlers.removeTab : this.handlers.applyTab;
                    case this.keys.DUPLICATE:
                        // Is CTRL or CMD (on Mac) pressed?
                        return (event.ctrlKey || event.metaKey) ? this.handlers.applyDuplication : false;
                    case this.keys.INDENT:
                        // Is CTRL or CMD (on Mac) pressed?
                        return (event.ctrlKey || event.metaKey) ? this.handlers.applyIndentation : false;
                    case this.keys.UNINDENT:
                        // Is CTRL or CMD (on Mac) pressed?
                        return (event.ctrlKey || event.metaKey) ? this.handlers.removeIndentation : false;
                    default:
                        // default would prevent the
                        // inhibition of default settings.
                        return false;
                }
            }
        };

        /**
         * Get either the height of an element as defined in style/CSS or its browser-computed height.
         *
         * @param {HTMLElement} element
         * @returns {number}
         */
        function getHeight(element) {
            return Math.max(// Maximum of computed or set heights.
                parseInt(window.getComputedStyle(element).height), // Height is not set in styles.
                (parseInt(element.style.height) || 0) // Property's own height if set, otherwise 0.
            );
        }

        /**
         * Update the height of an element based on its scroll height.
         *
         * @param {HTMLTextAreaElement} editor
         * @returns {HTMLTextAreaElement}
         */
        function updateHeight(editor) {
            // Ensure that the editor is resizable before anything else.
            // Change size if scroll is larger that height, otherwise do nothing.
            if (editor.scrollTop)
                editor.style.height = editor.scrollTop + getHeight(editor) + "px";
            return editor;
        }

        /**
         * @example
         *
         *     let element = document.getElementsByClassName('markdownx');
         *
         *     new MarkdownX(
         *         element,
         *         element.querySelector('.markdownx-editor'),
         *         element.querySelector('.markdownx-preview')
         *     )
         *
         * @param {HTMLElement} parent - Markdown editor element.
         * @param {HTMLTextAreaElement} editor - Markdown editor element.
         * @param {HTMLElement} preview - Markdown preview element.
         */
        var MarkdownX = function (parent, editor, preview) {
            var _this = this;
            /**
             * MarkdownX properties.
             */
            var properties = {
                editor: editor,
                preview: preview,
                parent: parent,
                _latency: null,
                _editorIsResizable: null
            };
            /**
             * Initialisation settings (mounting events, retrieval of initial data,
             * setting animation properties, latency, timeout, and resizability).
             *
             * @private
             */
            var _initialize = function () {
                _this.timeout = null;
                // Events
                // ----------------------------------------------------------------------------------------------
                var documentListeners = {
                    object: document,
                    listeners: [
                        {type: "drop", capture: false, listener: EventHandlers.inhibitDefault},
                        {type: "dragover", capture: false, listener: EventHandlers.inhibitDefault},
                        {type: "dragenter", capture: false, listener: EventHandlers.inhibitDefault},
                        {type: "dragleave", capture: false, listener: EventHandlers.inhibitDefault}
                    ]
                }, editorListeners = {
                    object: properties.editor,
                    listeners: [
                        {type: "drop", capture: false, listener: onDrop},
                        {type: "input", capture: true, listener: inputChanged},
                        {type: "keydown", capture: true, listener: onKeyDown},
                        {type: "dragover", capture: false, listener: EventHandlers.onDragEnter},
                        {type: "dragenter", capture: false, listener: EventHandlers.onDragEnter},
                        {type: "dragleave", capture: false, listener: EventHandlers.inhibitDefault},
                        {type: "compositionstart", capture: true, listener: onKeyDown}
                    ]
                };
                // Initialise
                // --------------------------------------------------------
                // Mounting the defined events.
                utils_1.mountEvents(editorListeners, documentListeners);
                properties.editor.setAttribute('data-markdownx-init', '');
                // Set animation for image uploads lock down.
                properties.editor.style.transition = "opacity 1s ease";
                properties.editor.style.webkitTransition = "opacity 1s ease";
                // Upload latency - must be a value >= 500 microseconds.
                properties._latency =
                    Math.max(parseInt(properties.editor.getAttribute(LATENCY_ATTRIBUTE)) || 0, LATENCY_MINIMUM);
                // If `true`, the editor will expand to scrollHeight when needed.
                properties._editorIsResizable = ((properties.editor.getAttribute(RESIZABILITY_ATTRIBUTE).match(/true/i) || []).length > 0 &&
                    properties.editor.offsetHeight > 0 &&
                    properties.editor.offsetWidth > 0);
                getMarkdown();
                utils_1.triggerCustomEvent("markdownx.init");
            };
            /**
             * settings for `timeout`.
             *
             * @private
             */
            var _markdownify = function () {
                clearTimeout(_this.timeout);
                _this.timeout = setTimeout(getMarkdown, properties._latency);
            };
            /**
             * Handling changes in the editor.
             */
            var inputChanged = function () {
                properties.editor = properties._editorIsResizable ?
                    updateHeight(properties.editor) : properties.editor;
                return _markdownify();
            };
            /**
             * Handling of drop events (when a file is dropped into `properties.editor`).
             *
             * @param {DragEvent} event
             */
            var onDrop = function (event) {
                if (event.dataTransfer && event.dataTransfer.files.length)
                    Object.keys(event.dataTransfer.files).map(function (fileKey) {
                        return sendFile(event.dataTransfer.files[fileKey]);
                    });
                EventHandlers.inhibitDefault(event);
            };
            /**
             * Handling of keyboard events (i.e. primarily hotkeys).
             *
             * @param {KeyboardEvent} event
             * @returns {Boolean | null}
             */
            var onKeyDown = function (event) {
                var handlerFunc = keyboardEvents.hub(event);
                if (typeof handlerFunc != 'function')
                    return false;
                EventHandlers.inhibitDefault(event);
                // Holding the start location before anything changes.
                var SELECTION_START = properties.editor.selectionStart;
                properties.editor.value = handlerFunc({
                    start: properties.editor.selectionStart,
                    end: properties.editor.selectionEnd,
                    value: properties.editor.value
                });
                _markdownify();
                properties.editor.focus();
                // Set the cursor location to the start location of the selection.
                properties.editor.selectionEnd = properties.editor.selectionStart = SELECTION_START;
                return false;
            };
            /**
             * Uploading the `file` onto the server through an AJAX request.
             *
             * @param {File} file
             */
            var sendFile = function (file) {
                properties.editor.style.opacity = UPLOAD_START_OPACITY;
                var xhr = new utils_1.Request(properties.editor.getAttribute(UPLOAD_URL_ATTRIBUTE), // URL
                    utils_1.preparePostData({image: file}) // Data
                );
                xhr.success = function (resp) {
                    var response = JSON.parse(resp);
                    if (response.image_code) {
                        insertImage(response.image_code);
                        utils_1.triggerCustomEvent('markdownx.fileUploadEnd', properties.parent, [response]);
                    } else if (response.image_path) {
                        // ToDo: Deprecate.
                        insertImage("![](\"" + response.image_path + "\")");
                        utils_1.triggerCustomEvent('markdownx.fileUploadEnd', properties.parent, [response]);
                    } else {
                        console.error(XHR_RESPONSE_ERROR, response);
                        utils_1.triggerCustomEvent('markdownx.fileUploadError', properties.parent, [response]);
                        return null;
                    }
                    properties.editor.style.opacity = NORMAL_OPACITY;
                };
                xhr.error = function (response) {
                    properties.editor.style.opacity = NORMAL_OPACITY;
                    console.error(response);
                    utils_1.triggerCustomEvent('fileUploadError', properties.parent, [response]);
                };
                return xhr.send();
            };
            /**
             * Uploading the markdown text from `properties.editor` onto the server
             * through an AJAX request, and upon receiving the HTML encoded text
             * in response, the response will be display in `properties.preview`.
             */
            var getMarkdown = function () {
                var xhr = new utils_1.Request(properties.editor.getAttribute(PROCESSING_URL_ATTRIBUTE), // URL
                    utils_1.preparePostData({content: properties.editor.value}) // Data
                );
                xhr.success = function (response) {
                    properties.preview.innerHTML = response;
                    properties.editor = updateHeight(properties.editor);
                    utils_1.triggerCustomEvent('markdownx.update', properties.parent, [response]);
                };
                xhr.error = function (response) {
                    console.error(response);
                    utils_1.triggerCustomEvent('markdownx.updateError', properties.parent, [response]);
                };
                return xhr.send();
            };
            /**
             * Inserts markdown encoded image URL into `properties.editor` where
             * the cursor is located.
             *
             * @param textToInsert
             */
            var insertImage = function (textToInsert) {
                properties.editor.value =
                    properties.editor.value.substring(0, properties.editor.selectionStart) + "\n\n" +
                    textToInsert +
                    ("\n\n" + properties.editor.value.substring(properties.editor.selectionEnd)); // Succeeding text.
                properties.editor.selectionStart =
                    properties.editor.selectionEnd =
                        properties.editor.selectionStart + textToInsert.length;
                utils_1.triggerEvent(properties.editor, 'keyup');
                inputChanged();
            };
            _initialize();
        };
        exports.MarkdownX = MarkdownX;
        (function (funcName, baseObj) {
            // The public function name defaults to window.docReady
            // but you can pass in your own object and own function
            // name and those will be used.
            // if you want to put them in a different namespace
            funcName = funcName || "docReady";
            baseObj = baseObj || window;
            var readyList = [], readyFired = false, readyEventHandlersInstalled = false;
            /**
             * Called when the document is ready. This function protects itself
             * against being called more than once.
             */
            var ready = function () {
                if (!readyFired) {
                    // Must be `true` before the callbacks are called.
                    readyFired = true;
                    // if a callback here happens to add new ready handlers,
                    // the docReady() function will see that it already fired
                    // and will schedule the callback to run right after
                    // this event loop finishes so all handlers will still execute
                    // in order and no new ones will be added to the readyList
                    // while we are processing the list
                    readyList.map(function (ready) {
                        return ready.fn.call(window, ready.ctx);
                    });
                    // allow any closures held by these functions to free
                    readyList = [];
                }
            };
            var readyStateChange = function () {
                return document.readyState === "complete" ? ready() : null;
            };
            // This is the one public interface
            // docReady(fn, context);
            // the context argument is optional - if present, it will be passed
            // as an argument to the callback
            baseObj[funcName] = function (callback, context) {
                // if ready has already fired, then just schedule the callback
                // to fire asynchronously, but right away
                if (readyFired) {
                    setTimeout(function () {
                        return callback(context);
                    }, 1);
                    return;
                } else {
                    // add the function and context to the list
                    readyList.push({fn: callback, ctx: context});
                }
                // If the document is already ready, schedule the ready
                // function to run.
                if (document.readyState === "complete") {
                    setTimeout(ready, 1);
                } else if (!readyEventHandlersInstalled) {
                    // otherwise if we don't have event handlers installed,
                    // install them first choice is DOMContentLoaded event.
                    document.addEventListener("DOMContentLoaded", ready, false);
                    // backup is window load event
                    window.addEventListener("load", ready, false);
                    readyEventHandlersInstalled = true;
                }
            };
        })("docReady", window);
        docReady(function () {
            var ELEMENTS = document.getElementsByClassName('markdownx');
            return Object.keys(ELEMENTS).map(function (key) {
                var element = ELEMENTS[key], editor = element.querySelector('.markdownx-editor'),
                    preview = element.querySelector('.markdownx-preview');
                // Only add the new MarkdownX instance to fields that have no MarkdownX instance yet.
                if (!editor.hasAttribute('data-markdownx-init'))
                    return new MarkdownX(element, editor, preview);
            });
        });

    }, {"./utils": 2}], 2: [function (require, module, exports) {
        "use strict";
        Object.defineProperty(exports, "__esModule", {value: true});

        /**
         * Looks for a cookie, and if found, returns the values.
         *
         * ... note:: Only the first item in the array is returned
         *            to eliminate the need for array deconstruction
         *            in the target.
         *
         * @param {string} name - The name of the cookie.
         * @returns {string | null}
         */
        function getCookie(name) {
            if (document.cookie && document.cookie.length) {
                var cookies = document.cookie
                    .split(';')
                    .filter(function (cookie) {
                        return cookie.indexOf(name + "=") !== -1;
                    })[0];
                try {
                    return decodeURIComponent(cookies.trim().substring(name.length + 1));
                } catch (e) {
                    if (e instanceof TypeError) {
                        console.info("No cookie with key \"" + name + "\". Wrong name?");
                        return null;
                    }
                    throw e;
                }
            }
            return null;
        }

        exports.getCookie = getCookie;

        /**
         * @example
         *
         *
         * @param rows
         * @returns
         */
        function zip() {
            var rows = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                rows[_i] = arguments[_i];
            }
            if (rows[0].constructor == Array)
                return rows[0].slice().map(function (_, c) {
                    return rows.map(function (row) {
                        return row[c];
                    });
                });
            // ToDo: To be updated to Objects.values in ECMA2017 after the method is fully ratified.
            var asArray = rows.map(function (row) {
                return Object.keys(row).map(function (key) {
                    return row[key];
                });
            });
            return asArray[0].slice().map(function (_, c) {
                return asArray.map(function (row) {
                    return row[c];
                });
            });
        }

        exports.zip = zip;

        /**
         *
         * @param collections
         * @returns
         */
        function mountEvents() {
            var collections = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                collections[_i] = arguments[_i];
            }
            return collections.map(function (events) {
                return events.listeners
                    .map(function (series) {
                        return events.object
                            .addEventListener(series.type, series.listener, series.capture);
                    });
            });
        }

        exports.mountEvents = mountEvents;

        /**
         *
         * @param {JSON} data
         * @param {Boolean} csrf
         * @returns {FormData}
         */
        function preparePostData(data, csrf) {
            if (csrf === void 0) {
                csrf = true;
            }
            var form = new FormData();
            if (csrf) {
                var csrfToken = getCookie('csrftoken');
                if (!csrfToken)
                    csrfToken = document.querySelector("input[name='csrfmiddlewaretoken']").value;
                form.append("csrfmiddlewaretoken", csrfToken);
            }
            Object.keys(data).map(function (key) {
                return form.append(key, data[key]);
            });
            return form;
        }

        exports.preparePostData = preparePostData;

        /**
         *
         * @returns {XMLHttpRequest}
         * @throws TypeError - AJAX request is not supported.
         */
        function AJAXRequest() {
            // Chrome, Firefox, IE7+, Opera, Safari
            // and everything else that has come post 2010.
            if ("XMLHttpRequest" in window)
                return new XMLHttpRequest();
            // ToDo: Deprecate.
            // Other IE versions (with all their glories).
            // Microsoft.XMLHTTP points to Msxml2.XMLHTTP and is
            // redundant - but you never know with Microsoft.
            try {
                return new ActiveXObject("Msxml2.XMLHTTP.6.0");
            } catch (e) {
            }
            try {
                return new ActiveXObject("Msxml2.XMLHTTP.3.0");
            } catch (e) {
            }
            try {
                return new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {
            }
            // Just throw the computer outta the window!
            alert("Your browser belongs to history!");
            throw new TypeError("This browser does not support AJAX requests.");
        }

        /**
         * Handles AJAX POST requests.
         */
        var Request = (function () {
            /**
             *
             * @param url
             * @param data
             */
            function Request(url, data) {
                this.xhr = AJAXRequest();
                this.url = url;
                this.data = data;
            }

            /**
             *
             * @param event
             */
            Request.prototype.progress = function (event) {
                if (event.lengthComputable)
                    console.log((event.loaded / event.total) * 100 + '% uploaded');
            };
            /**
             *
             * @param response
             */
            Request.prototype.error = function (response) {
                console.error(response);
            };
            /**
             *
             * @param response
             */
            Request.prototype.success = function (response) {
                console.info(response);
            };
            /**
             *
             */
            Request.prototype.send = function () {
                var _this = this;
                var SUCCESS = this.success, ERROR = this.error, PROGRESS = this.progress;
                this.xhr.open('POST', this.url, true);
                this.xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
                this.xhr.upload.onprogress = function (event) {
                    return PROGRESS(event);
                };
                this.xhr.onerror = function (event) {
                    ERROR(_this.xhr.responseText);
                };
                this.xhr.onload = function (event) {
                    var data = null;
                    if (_this.xhr.readyState == XMLHttpRequest.DONE) {
                        if (!_this.xhr.responseType || _this.xhr.responseType === "text") {
                            data = _this.xhr.responseText;
                        } else if (_this.xhr.responseType === "document") {
                            data = _this.xhr.responseXML;
                        } else {
                            data = _this.xhr.response;
                        }
                    }
                    SUCCESS(data);
                };
                this.xhr.send(this.data);
            };
            return Request;
        }());
        exports.Request = Request;

        /**
         *
         * @param {Element} element
         * @param {string} type
         */
        function triggerEvent(element, type) {
            // modern browsers, IE9+
            var event = document.createEvent('HTMLEvents');
            event.initEvent(type, false, true);
            element.dispatchEvent(event);
        }

        exports.triggerEvent = triggerEvent;

        /**
         *
         * @param {string} type
         * @param {Element | Document} element
         * @param {any} args
         */
        function triggerCustomEvent(type, element, args) {
            if (element === void 0) {
                element = document;
            }
            if (args === void 0) {
                args = null;
            }
            // modern browsers, IE9+
            var event = new CustomEvent(type, {'detail': args});
            element.dispatchEvent(event);
        }

        exports.triggerCustomEvent = triggerCustomEvent;

        /**
         *
         * @param {Element} element
         * @param {string[]} className
         */
        function addClass(element) {
            var className = [];
            for (var _i = 1; _i < arguments.length; _i++) {
                className[_i - 1] = arguments[_i];
            }
            className.map(function (cname) {
                if (element.classList)
                    element.classList.add(cname);
                else {
                    var classes = element.className.split(' ');
                    if (classes.indexOf(cname) < 0)
                        classes.push(cname);
                    element.className = classes.join(' ');
                }
            });
        }

        exports.addClass = addClass;

        /**
         *
         * @param {Element} element
         * @param {string[]} className
         */
        function removeClass(element) {
            var className = [];
            for (var _i = 1; _i < arguments.length; _i++) {
                className[_i - 1] = arguments[_i];
            }
            className.map(function (cname) {
                if (element.classList)
                    element.classList.remove(cname);
                else {
                    var classes = element.className.split(' '), idx = classes.indexOf(cname);
                    if (idx > -1)
                        classes.splice(idx, 1);
                    element.className = classes.join(' ');
                }
            });
        }

        exports.removeClass = removeClass;

    }, {}]
}, {}, [1]);
