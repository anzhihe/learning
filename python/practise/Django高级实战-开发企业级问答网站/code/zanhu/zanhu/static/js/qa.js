$(function () {

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

    function csrfSafeMethod(method) {
        // These HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var csrftoken = getCookie('csrftoken');
    var page_title = $(document).attr("title");
    // This sets up every ajax call with proper headers.
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $("#publish").click(function () {
        // function to operate the Publish button in the question form, marking
        // the question status as published.
        $("input[name='status']").val("O");
        $("#question-form").submit();
    });

    $("#draft").click(function () {
        // Function to operate the Draft button in the question form, marking
        // the question status as draft.
        $("input[name='status']").val("D");
        $("#question-form").submit();
    });

    $(".question-vote").click(function () {
        // Vote on a question.
        var span = $(this);
        var question = $(this).closest(".question").attr("question-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/question/vote/',
            data: {
                'question': question,
                'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
                $('.vote', span).removeClass('voted');
                if (vote === "U") {
                    $(span).addClass('voted');
                }
                $("#questionVotes").text(data.votes);
            }
        });
    });

    $(".answer-vote").click(function () {
        // Vote on an answer.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/answer/vote/',
            data: {
                'answer': answer,
                'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
                $('.vote', span).removeClass('voted');
                if (vote === "U") {
                    $(span).addClass('voted');
                }
                $("#answerVotes").text(data.votes);
            }
        });
    });

    $("#acceptAnswer").click(function () {
        // Mark an answer as accepted.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        $.ajax({
            url: '/qa/accept-answer/',
            data: {
                'answer': answer
            },
            type: 'post',
            cache: false,
            success: function (data) {
                $("#acceptAnswer").removeClass("accepted");
                $("#acceptAnswer").prop("title", "点击接受回答");
                $("#acceptAnswer").addClass("accepted");
                $("#acceptAnswer").prop("title", "该回答已被采纳");
            }
        });
    });
});
